#!/usr/bin/env python3

print (dir(str),"\n")

x="JumP"
print(dir(x), "\n")


print ("Convert string to lower case:",x.lower(),  sep=" ")
print ("Convert string to lower case:",x.upper(), sep=" ")

x="JumP"
print ("Convert first two character to UPPER and last two to lower case:", x[0:2].upper() + x[2:4].lower(), sep=" ")

print (len(x)%2)

