#!/usr/bin/env python3
# open file in read mode
dnsfile = open("dnsservers.txt", "r")
# create list of lines
dnslist = dnsfile.readlines()
# loop over lines
for namesvr in dnslist:
    #print and end without a newline
    print(namesvr, end="")
# close your file
dnsfile.close()
