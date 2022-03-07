import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter url >>>")
print("Retrieving", url)

uh = urllib.request.urlopen(url)
data = uh.read().decode()

js = json.loads(data)
print("Retrieved", len(data),"characters")


count = []

# print(js["comments"][0])

for item in js["comments"]:
    count.append(int(item["count"]))

print("Count:", len(count))
print("Sum:", sum(count))