# Extract Data from JSON
import json, urllib.request
url = input('Enter URL:')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_1465666.json'
data = urllib.request.urlopen(url).read().decode()             # URL Request/Open()/Read()/Decode()
total = []
info = json.loads(data)

#  print(json.dumps(info, indent=4))                           # print JSON in readable form for Analysis
print(len(data), 'Characters found')
for i in info['comments']:                                     # iterate for every element in 'comments'
    total.append(i['count'])                                   # append contnents of 'count' to 'total' - (list)

print('Sum of "comments":', sum(total))
 