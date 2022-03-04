import urllib.parse, urllib.request, urllib.error
from bs4 import BeautifulSoup

url = input("Enter url >>>")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# getting all the anchor tags
tags = soup("a")
for tag in tags:
    print(tag.get("href", None))

# http://www.dr-chuck.com/page1.html
# http://www.dr-chuck.com/page2.html