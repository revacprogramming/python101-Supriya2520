# Lists
#ex 8.5
fname = input("Enter file name: ")
x = open(fname)
count = 0
for line in x:
    y = line.find('From ')
    if y >= 0:
        print (line.split()[1])
        count += 1

print("There were", count, "lines in the file with From as the first word")





























