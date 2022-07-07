#using web services
#Extracting Data from XML
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
while True:
    url = input('Enter location: ')
    if len(url) < 1: break
    xml = urllib.request.urlopen(url, context=ctx).read()
    print('Retrieving', url)
    print('Retrieved', len(xml), 'characters')
    commentinfo = ET.fromstring(xml)
    lst = commentinfo.findall('comments/comment')
    sum = 0
    count = 0
    for item in lst:
        count = count + 1
        sum = sum + int(item.find('count').text)
    print('Count:', count)
    print('Sum:', sum)

