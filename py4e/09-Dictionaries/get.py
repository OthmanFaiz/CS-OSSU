uinput = input("Enter a line of text >>>")
count = {}

words = uinput.split()
print("Words:", words)

print("Counting...")

for word in words:
    count[word] = count.get(word, 0) +1

print(count)