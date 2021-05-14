#!/usr/bin/env python3
import urllib.request
import re

 
def search(searchfor,url):
    searchMe = urllib.request.urlopen(url).read().decode("utf-8")
    return searchMe

def getinput():
    try:
        words2search = []

        while words != "q" and searchFor != "q":
            print("Where should we search? or enter q to quit")
            words2search.append(input())
            #split url
            if url == "q":
                break
            print("Great! So we'll try to open this url " + str(url) + " to search for the phrase: or enter q to quit")
            searchFor = input()
            if searchFor == "q":
                break
            return list of words to look for




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

