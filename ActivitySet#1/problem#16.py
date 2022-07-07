#import modules

import urllib.request

import urllib.error

import urllib.parse

from bs4 import BeautifulSoup

import ssl

 

# Https protocol, for those you didn't understood this is when we put https instead of http

ctx = ssl.create_default_context()

ctx.check_hostname = False

ctx.verify_mode = ssl.CERT_NONE

 

url = input('Enter - ')

html = urllib.request.urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, 'html.parser')

 

#we create a list here as we'll store all values in the list and then print the sum of list

lst = list()

#have to target span tag as given in assignment

tags = soup('span')

for tag in tags:

    Contents = tag.contents[0]

    c = int(Contents)

    lst.append(c)

print(sum(lst))

 







