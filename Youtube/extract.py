#!/usr/bin/python

import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/playlist?list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK'
web = requests.get(url)
data = web.content
soup = BeautifulSoup(data, 'html.parser')

video = soup.findAll('a', {'class':'pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link '})
for data in video:
    title = data.text.strip()
    link = data.get('href')

    print 'Title = ' + title
    print 'Link = https://www.youtube.com' + link
    print


