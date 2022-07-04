# Files
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
x = 0
count =0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    y=line.find('0.')
    z =float(line[y:])
    x = x+z
    count = count+1
avg=x/count
print("Average spam confidence:",avg)










































