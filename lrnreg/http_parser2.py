#!/usr/bin/env python3
import urllib.request
import re


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

    if re.search(searchFor, searchMe):
        print("Found a match!")
    else:
        print("No match!")

