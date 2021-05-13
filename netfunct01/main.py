#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""
import crayons
# function to push commands
def commandpush(devicecmd): # devicecmd==list
    for cmd in devicecmd.keys():
        print('Handshaking. .. ... connecting with ' + cmd )
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[cmd]:
            print('Attempting to send command --> ' + mycmds )
            # we'll learn to write code that sends cmds to device here

# function to push commands
def device_reboot(devices2reboot): # devicecmd==list
    for ipaddr in device2reboot.keys():
        print('Handshaking. .. ... connecting with ' + ipaddr )
        for configcmd in device2reboot[ipaddr]:
            print('Attempting to send command --> ' + configcmd )


# start our main script
def main():
    work2do = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} 
    # data that replaces data stored in file

    print (crayons.red("Welcome to the network device command pusher")) # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(work2do) # call function to push commands to devices
    device_reboot(work2do)

# call our main function
main()

