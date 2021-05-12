#!/usr/bin/python3
#Credit => https://www.geeksforgeeks.org/extract-ip-address-from-file-using-python/
import re

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
ipv4_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

ipaddrs=[]
# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            ipaddrs.append(ipv4_pattern.search(line)[0])
            loginfail += 1 # this is the same as loginfail = loginfail + 1

print("The number of failed log in attempts is", loginfail)
print("Problem IP adddresses below:")
for ipaddr in ipaddrs:
    print(ipaddr)

