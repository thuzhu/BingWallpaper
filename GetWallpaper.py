path = 'D:\\BingWallpaper'

import urllib.request
import json

url = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=2&mkt=en-US'
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
page = response.read()
hJson = json.loads(page)
wallPaperUrl = 'https://www.bing.com/' + hJson['images'][0]['url']
startDate = hJson['images'][0]['startdate']
urllib.request.urlretrieve(wallPaperUrl, path + "\\BingWallpaper\\" + startDate + '.jpg')