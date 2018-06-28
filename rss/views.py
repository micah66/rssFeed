from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect
import feedparser as f
import json
from datetime import datetime
from .models import Headlines
from . import forms

# Create your views here.
def base(request):
    return render(request, 'rssFeed/base.html')

def welcome(request):
    return render(request, 'rssFeed/welcome.html')

@csrf_protect
def get_feed(request):
    if request.method == 'POST':
        result = search_criteria_form(request)
    else:
        feed = f.parse('http://mlb.mlb.com/partnerxml/gen/news/rss/nyy.xml')
        result = [i for i in feed['entries'] if i['link']]
        for i in result:
            author = i.get("author", 'Unknown')
            new_headline = Headlines(title=i.title, link=i.link, time_added=timezone.now(), author=author, published=i.published)
            new_headline.save()
    refreshed = request.COOKIES.get('refresh_count')
    if request.COOKIES.get('refresh_count'):
        message = f'Welcome back! The headlines were lasted refreshed at: {datetime.now()}'
    else:
        message = 'Welcome!'
    context = {
        'data': result,
        'cookies': message,
        'range': range(10)
    }
    response = render(request, 'rssFeed/rss.html', context)
    response.set_cookie('refresh_count', message)
    return response


def search_criteria_form(request):
    search = request.POST.get('search_criteria')
    search = search.split(' ')
    result = Headlines.objects.all()
    for word in search:
        result = result.filter(title__icontains=word)
    return result
