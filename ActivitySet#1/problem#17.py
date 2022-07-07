import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# Ignore certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# Open the original URL
url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# Read the count and position from the user
count = input('Enter count: ')
position = input('Enter position: ')
print('Retrieving:', url)
# The iteration
for i in range(int(count)):
    tags = soup('a')
    urlpos = tags[int(position) - 1]
    url = urlpos.get('href', None)
    print('Retrieving:', url) # and then open the target URL in each page
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')







