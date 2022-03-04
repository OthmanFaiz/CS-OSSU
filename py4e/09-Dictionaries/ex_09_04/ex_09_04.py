# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = input("Enter file name: ")
fh = open(fname)
count = {}
mails = []

for line in fh:
    if line.startswith("From "):
        mails.append(line.split()[1])

for mail in mails:
    count[mail] = count.get(mail, 0) + 1

mostSentEmail = None
numSentEmail = None

for email,num in count.items():
    if numSentEmail is None or num > numSentEmail:
        mostSentEmail = email
        numSentEmail = num

print(mostSentEmail,numSentEmail)