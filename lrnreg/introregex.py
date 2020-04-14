#!/usr/bin/env python3
import urllib.request
import re

print("Where should we search?")
url = input()
searchFor = input("Great! So we'll try to open this url " + (url) + "to search for the phrase:")
searchMe = urllib.request.urlopen(url).read().decode("utf-8")

if re.search(searchFor, searchMe):
    print("Found a match!")
else:
    print("No match!")
