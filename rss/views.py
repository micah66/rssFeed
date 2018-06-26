from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
import feedparser as f
import json
from datetime import datetime
from .models import Headlines

# Create your views here.
def welcome(request):
    return render(request, 'rssFeed/welcome.html')


def get_feed(request):
    feed = f.parse('http://mlb.mlb.com/partnerxml/gen/news/rss/nyy.xml')
    feed_list = [i for i in feed['entries'] if i['link']]
    for i in feed_list:
        author = i.get("author", 'Unknown')
        new_headline = Headlines(title=i.title, link=i.link, time_added=timezone.now(), author=author, published=i.published)
        new_headline.save()
    refreshed = request.COOKIES.get('refresh_count')
    if request.COOKIES.get('refresh_count'):
        message = f'Welcome back! The headlines were lasted refreshed at: {datetime.now()}'
    else:
        message = 'Hello stranger!'
    context = {
        'data': feed_list,
        'cookies': message,
        'range': range(10)
    }
    response = render(request, 'rssFeed/rss.html', context)
    response.set_cookie('refresh_count', message)
    return response
