import urllib.parse, urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url >>>")
ipos = input("Enter position >>>")
pos = int(ipos) - 1
icount = input("Enter Count >>>")
count = int(icount)

urls = []

def conn(url,pos):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")    
    tags = soup("a")
    answer = tags[pos].get("href", None)
    urls.append(answer)
    return answer

print("Retrieving:",conn(url,pos))

for i in range(count - 1):
    print("Retrieving:",conn(urls[i],pos))

# print(urls)
# tomorrow will fix it

# print(answer)