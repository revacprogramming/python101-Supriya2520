# Tuples
filename = "dataset/mbox-short.txt"
name = input("Enter file:")

if len(name) < 1:
    name = "mbox-short.txt"
counts = {}
handle = open(name)
for line in handle:
    if not line.startswith('From '):
        continue
    x = line.replace(':',' ')
    words = x.split()
    y = words[5:6]
    for word in y:
        counts[word] = counts.get(word,0) + 1
lst = []






















