#!/usr/bin/env python3
    
def validIP(address):
    parts = address.split(".")
    if len(parts) != 4:
        return False 
    if parts[3] == "1":
        return False  
    for item in parts:
        if item.isalpha():
            return False
        if not 0 <= int(item) <= 255:
            return False
    return True
        
ipchk = input("Apply an IP address: ") # prompts the user for input
if validIP(ipchk):
    parts = ipchk.split(".")
    print(int(parts[0]),int(parts[1]),int(parts[2]),int(parts[3]),sep=".",end=" " )
    print("is VALID!")
else:
    print ("the ip is not valid", ipchk)