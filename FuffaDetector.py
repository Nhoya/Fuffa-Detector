#!/usr/bin/env python3
import urllib.request
from bs4 import BeautifulSoup
import sys
import re
try:
    url = sys.argv[1]
except IndexError:
    print("Usage:\n FuffaDetector.py [url]")
    exit(2)
try:
    html = urllib.request.urlopen(url).read()
except ValueError:
    print("Invalid Url")
    exit(2)

soup = BeautifulSoup(html, "lxml")
for script in soup(["script","ul", "li", "a","style","meta","br","h1","h2","h3","h4","h5","h6","span"]):
    script.extract()
text = soup.get_text()
lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
text = '\n'.join(chunk for chunk in chunks if chunk)


regex = r"cyber*"
matches = re.finditer(regex,text,re.IGNORECASE)

for cyberNum, cyber in enumerate(matches):
    cyberNum = cyberNum + 1

if cyberNum == 0:
    print("Probably No fuffa inside")
elif cyberNum <= 3:
    print("Fuffa inside")
elif cyberNum >= 4:
    print("High quantity of fuffa")

