import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("Enter url >>>")

uh = urllib.request.urlopen(url)
data = uh.read().decode()

print("Retrieving", url)
print("Retrieved", len(data),"characters")

tree = ET.fromstring(data)
counts = tree.findall('comments/comment')

count = []
for item in counts:
    count.append(int(item.find("count").text))
print("Count:",len(count))
print("Sum:",sum(count))