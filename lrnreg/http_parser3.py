#!/usr/bin/env python3
import urllib.request
import re

found=0
url=""
searchFor=""
while url != "q" and searchFor != "q":
    print("Where should we search? or enter q to quit")
    url = input()
    if url == "q":
        break
    print("Great! So we'll try to open this url " + str(url) + " to search for the phrase: or enter q to quit")
    searchFor = input()
    if searchFor == "q":
        break
    searchMe = urllib.request.urlopen(url).read().decode("utf-8")

    #found=found+1

    if re.search(searchFor, searchMe):
        found=found+1
        print(found,"matches found!")
    else:
        print("No match found!")

