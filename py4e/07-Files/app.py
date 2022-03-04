fileHandle = open("text.txt", "r")

for line in fileHandle:
    if not line.startswith("print"):
        continue
    print(line.rstrip())
