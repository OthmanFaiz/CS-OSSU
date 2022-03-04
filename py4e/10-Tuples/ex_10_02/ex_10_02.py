# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input("Enter file name >>>")
fh = open(fname)

hours = []

for line in fh:
    if line.startswith("From "):
        hours.append(line.split()[5].split(":")[0])

count = {}

for time in hours:
    count[time] = count.get(time, 0) + 1

# print(sorted((hours,time) for hours,time in count.items()))
for hour, time in sorted(count.items()):
    print(hour,time)