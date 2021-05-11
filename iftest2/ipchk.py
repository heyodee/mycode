#!/usr/bin/env python3                                                      
                                                                            
def validIP(address):                                                       
    parts = address.split(".")                                              
    if len(parts) != 4:                                                     
        return False                                                        
    if parts[3] == "1":                                                     
        return False                                                        
    for item in parts:                                                      
        if not 0 <= int(item) <= 255:                                       
            return False                                                    
    return True                                                             
                                                                            
ipchk = input("Apply an IP address: ") # prompts the user for input         
#ipchk == "*.*.*.1":                                                        
if validIP(ipchk):                                                          
    print ("the ip is valid", ipchk)                                        
    parts = ipchk.split(".")                                              
    print(int(parts[0]),int(parts[1]),int(parts[2]),int(parts[3]),sep=".")  
else:                                                                       
    print ("the ip is not valid", ipchk)                                    
                                                                            
#else: # if data is NOT provided                                            
#   print("You did not provide input.") # indented under else  