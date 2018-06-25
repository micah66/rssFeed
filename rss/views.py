from django.shortcuts import render
from django.http import HttpResponse
import feedparser as f
import json
from datetime import datetime


# Create your views here.
def index(request):
    return render(request, 'rssFeed/index.html')


def get_feed(request):
    feed = f.parse('http://mlb.mlb.com/partnerxml/gen/news/rss/nyy.xml')
    feed_list = [i for i in feed['entries'] if i['link']]
    refreshed = request.COOKIES.get('refresh_count')
    if request.COOKIES.get('refresh_count'):
        message = f'Welcome back! The headlines were lasted refreshed at: {datetime.now()}'
    else:
        message = 'Welcome!'
    get_feed_data = {
        'data': feed_list,
        'cookies': message
    }
    response = HttpResponse(json.dumps(get_feed_data))
    response.set_cookie('refresh_count', message)
    return response
