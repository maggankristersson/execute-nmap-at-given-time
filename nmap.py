import os
import datetime
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

def executeScript():
    ip_addr = [
        "8.8.8.8",
        "8.8.4.4"
    ]
    flags = [
        "-T5",
        "-Pn"
    ]
    os.system("sudo tshark -vv -w networktraffic.cap &")
    for i in range(len(ip_addr)):
        #Replace "." with "-" in IP adderss
        ip_address = str(ip_addr[i].replace(".", "-"))
        #Create folders for the IP-address       
        os.system("mkdir IP_" + ip_address)
        for j in range(len(flags)):
            #The nmap command
            command = "sudo nmap " +  str(ip_addr[i]) + " " + str(flags[j])

            #The name of the outputfiles
            executionTime = str(datetime.datetime.now())[8:16].replace(" ", "").replace(":", "") #Timenumber (Tidsnummer)
            outputFileName = "OUT" + ip_address + "" + flags[j][1:] + "" + executionTime + ""
            
            
            #Execute nmap. Place 
            print("Performing scan [" + str(j) + "] on " + ip_addr[i])
            os.system(str(command + " -oA ./IP_" + ip_address + "/" + outputFileName))         #Execute nmap
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
    os.system("sudo rm -rf IP_*")

    title = open("./resources/title.txt", "r")
    print(Fore.RED + title.read())
    print(Fore.GREEN + "Enter a time for the script to be executed (Format: HH:MM:SS):")
    execTime = input(" >> ")
    print(Fore.GREEN + "Script started! Executing at " + Fore.RED + execTime + Fore.GREEN + "...")
    print(Fore.GREEN + "Will capture traffic meanwhile script is running")
    execAtTime(execTime)

main()
