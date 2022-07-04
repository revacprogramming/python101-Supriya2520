# Lists
#ex 8.4
fname = input("Enter file name: ")
fh = open(fname)
list1 = list()
list2 = list()

for line in fh:
    x = line.split()
    list1 = list1 + x

for justone in list1:
    if justone not in list2:
        list2.append(justone)

print(sorted(list2))




























