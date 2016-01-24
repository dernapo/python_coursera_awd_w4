# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
count = raw_input('Enter count: ')
position = raw_input('Enter position: ')

#url = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Lancelot.html'
#count = 7
#position = 18

for i in range(0,count):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    # Retrieve all of the anchor tags
    tags = soup('a')
    # Get the url of the given position
    print 'Retrieving: ', url
    url = tags[position-1].get('href', None)
print 'Last Url: ', url
