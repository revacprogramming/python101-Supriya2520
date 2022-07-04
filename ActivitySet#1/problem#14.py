# regular exppression
import re
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print("File not found!")
    quit()
numlist = []
for line in fhand:
    num_in_line = re.findall('[0-9]+', line)
    if len(num_in_line) < 1 : continue
    for num in num_in_line:
        num = int(num)
        numlist.append(num)
print(sum(numlist))



 