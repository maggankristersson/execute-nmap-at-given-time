import os
import datetime


def executeScript():
    ip_addr = [
        "8.8.8.8",
        "8.8.4.4"
    ]
    flags = [
        "-T5",
        "-Pn"
    ]
    for i in range(len(ip_addr)):
        for j in range(len(flags)):
            #The nmap command
            command = "nmap " +  str(ip_addr[i]) + " " + str(flags[j])

            #The name of the outputfiles
            executionTime = str(datetime.datetime.now())[8:16].replace(" ", "").replace(":", "") #Timenumber (Tidsnummer)
            ip_address = str(ip_addr[i].replace(".", "-"))       #Replace "." with "-" in IP adderss
            outputFileName = "OUT[" + ip_address + "[" + flags[j][1:] + "]](" + executionTime + ")"

            #Create folders for the IP-address
            os.system("mkdir IP()" + ip_address + ")")
            #Execute nmap. Place 
            os.system(str(command + " -oA " + outputFileName))         #Execute nmap
        
        
        

def execAtTime(execTime):
    haveNotExecuted = True
    while haveNotExecuted:
        timefull = str(datetime.datetime.now())
        clock = timefull[11:19]
        if(execTime == clock):
            executeScript()
            haveNotExecuted = False


def main():
    os.system("del out*")
    execTime = "13:19:15"             #CHANGE ME
    print("Starting script...")
    execAtTime(execTime)

main()