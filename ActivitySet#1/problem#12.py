# Dictionaries
files  = open("mbox-short.txt")
for line in files:
    if line.startswith("From"):
        words = line.split()

        if len(words) > 6:
            counts[words[1]] = counts.get(words[1], 0) + 1
bigcount = None
bigword = None

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word
        
print(bigword, bigcount)




























































