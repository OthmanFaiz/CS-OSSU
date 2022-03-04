import urllib.parse, urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url >>>")
ipos = input("Enter position >>>")
pos = int(ipos)
icount = input("Enter Count >>>")
count = int(icount)

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup("a")
answer = tags[pos].get("href", None)
for i in range(count):
    html1 = urllib.request.urlopen(answer, context=ctx).read()
    soup1 = BeautifulSoup(html1, "html.parser")
    tags1 = soup("a")
    answer = tags1[pos].get("href", None)

# tomorrow will fix it

print(answer)