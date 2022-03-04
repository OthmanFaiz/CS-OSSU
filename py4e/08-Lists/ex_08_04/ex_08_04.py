fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    lineS = line.split()
    for word in lineS:
        if word in lst:
            continue
        lst.append(word)
lst.sort()
print(lst)