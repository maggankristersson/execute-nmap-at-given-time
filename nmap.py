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
    os.system("sudo tcpdump -vv -w networktraffic.cap &")
    for i in range(len(ip_addr)):
        for j in range(len(flags)):
            #The nmap command
            command = "sudo nmap " +  str(ip_addr[i]) + " " + str(flags[j])

            #The name of the outputfiles
            executionTime = str(datetime.datetime.now())[8:16].replace(" ", "").replace(":", "") #Timenumber (Tidsnummer)
            ip_address = str(ip_addr[i].replace(".", "-"))       #Replace "." with "-" in IP adderss
            outputFileName = "OUT(" + ip_address + "(" + flags[j][1:] + "))(" + executionTime + ")"

            #Create folders for the IP-address
            os.system("mkdir" + ip_address)
            #Execute nmap. Place 
            os.system(str(command + " -oA " + outputFileName))         #Execute nmap
    os.system("sudo pkill -9 -f tcpdump")
        
        
        

def execAtTime(execTime):
    haveNotExecuted = True
    while haveNotExecuted:
        timefull = str(datetime.datetime.now())
        clock = timefull[11:19]
        if(execTime == clock):
            executeScript()
            haveNotExecuted = False


def main():
    os.system("sudo rm out*")

    execTime = "13:19:15"             #CHANGE ME

    title = open("./resources/title.txt", "r")
    print(title.read())
    print("Enter a time for the script to be executed (Format: HH:MM:SS):")
    execTime = input(" >> ")
    print("Script started! Executing at " + execTime + "...")
    print("Will capture traffic meanwhile script is running")
    execAtTime(execTime)

main()
