#!/bin/python3

import importlib
import time
import requests
import banner
import os


# COLORS
G = '\033[1;34m[*] \033[0m'
S = '\033[1;32m[+] \033[0m'
W = '\033[1;33m[!] \033[0m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'


print("\n"+W + " If You Run This Tool First Time For SetUp Type 'install' For Commands Type 'help' Please!")

WhiteBox = True
while WhiteBox:
    
    # System Commands
    info   = "help"    # Help Menu
    get    = "install" # Setting up to tool
    ext    = "exit"    # exit to whitebox-framework
    clean  = "clear"   # Clean the console
    author = "about"   # About the author

    # Modules Commands
    shm   = "show modules"  # For Modules Command
    st    = "set target"    # Set the target 
    showT = "show target"   # Show the target
    exp   = "exploit"       # Exploit the victim
    
    # Modules
    chekhost = "use check_host"
    smbscann = "use smb_scanner"
    dnsscan  = "use dns_scanner"
    
    # WhiteBox-Framework
    wbterm = input("\nWhiteBox:~# ")
    
    # WBTerm Commands Start
    if wbterm == info:
        print("\n# Basic WhiteBox Commands")
        print("----------------------------------------------------------------")
        print("\nhelp         # Help Menu")
        print("install      # Set-Up The Tool")
        print("clear        # Clean The Terminal")
        print("exit         # Exit The Tool")
        print("about        # About of author")
    
        print("\n# Modules Commands")
        print("----------------------------------------------------------------")
        print("\nuse          # for selecet module")
        print("back         # Back to whitebox command line")
        print("set target   # Open settings for target")
        print("run          # Run for seceted module")
        print("commands     # Commands for which module seleceted")
        
        print("\n# Modules")
        print("------------------------------------------")
        print("\ncheck_host  # Host Checking for Up or Down!")
        print("smb_scanner # Scan For SMB")
        print("dns_scanner # Scan For sublists")
    

    elif wbterm == get:
        import install
    
    elif wbterm == author:
        print(WARNING + "\n# About The Author")
        print("-------------------------------------------------")
        print("\n# WhiteBox-Framework")
        print("# Author : Alperen Ergel")
        print("# Contact : alperen.ergel@yandex.com")
        print("# Twitter : @alpern_ae")
        print("# Instagram: @alperen_ae")
        print("# Web Site: https://alperenae.gitbook.io")
        print("# Project Github : https://github.com/Alperenae/whitebox-framework")
        print("# Other Projects : https://github.com/Alperenae" + ENDC)
    
    elif wbterm == clean:
        os.system("clear")
    
    elif wbterm == ext:
        exit()
    
    # Modules & Modules Commands
    elif wbterm == chekhost:  # Check Host Module
        chekhost = True
        while chekhost:
            ch = input("\nWhiteBox:~#" + FAIL + "(check_host) > " + ENDC )
            
            if ch == "set target":
                targ = input("Check Host: ") # Get Host And Check Host for it is up!
            
            elif ch == "show target":
                print(OKGREEN + "\nTarget: " + ENDC + targ)

            elif ch == "run":
                host = requests.get(targ)
                if host.status_code == 200:
                    print("\n" + G + "Waiting For Response" + ENDC)
                    time.sleep(3)
                    print("\n" + S+"Looks Like Host Up!")
                else:
                    print("")
                    print("\n" + FAIL + "[-] Looks Like Host Down!")
            
            elif ch == "commands":  # Commands for this module
                print("\n# Commands For check_host")
                print ("--------------------------")
                print("set target   # Set The Url For Check")
                print("show target  # Showing Which Target Selected")
                print("back         # Back To WhiteBox Term")
                print("run          # Start Checking Host For Up or Down")
            
            elif ch == "back": # Back to whitebox term
                break

            elif ch == "clear":
                os.system("clear")

            elif ch == "exit":
                exit()
    
    # SMB SCANNER MODULE
    elif wbterm == smbscann:
        smb_scanner = True
        while smb_scanner:
            sbs = input("\nWhiteBox:~#" + FAIL + "(smb_scanner) > " + ENDC )
            
            if sbs == "set target":
                targ = input("Target Ip or Domain: ")
            
            elif sbs == "show target":
                print(OKGREEN + "\nTarget: " + ENDC + targ)

            elif sbs == "run":
                host = targ
                print("\n" + G + "Waiting Results\n" + ENDC)
                time.sleep(2)
                os.system("nmap -p 445 -oN reports/smb/report.txt " + targ + " > /dev/null")
                print("\n# Port Satutus of " + targ)
                print("-------------------------------------------------------------")
                print("")
                os.system("sed -n '5,6'p reports/smb/report.txt")
                print("\n-------------------------------------------------------------\n")
            
            elif sbs == "commands":  # Commands for this module
                print("\n# Commands For check_host")
                print ("--------------------------")
                print("set target   # Set The Url For Check")
                print("show target  # Showing Which Target Selected")
                print("back         # Back To WhiteBox Term")
                print("run          # Start Checking Host For Up or Down")
            
            elif sbs == "back": # Back to whitebox term
                break

            elif sbs == "clear":
                os.system("clear")

            elif sbs == "exit":
                exit()
    
    # DNS_SCANNER
    elif wbterm == dnsscan:
        dnsscan = True
        while dnsscan:
            scan = input("\nWhiteBox:~#" + FAIL + "(dns_scanner) > " + ENDC )
            
            if scan == "set target":
                targ = input("Target Ip or Domain: ")
            
            elif scan == "show target":
                print(OKGREEN + "\nTarget: " + ENDC + targ)

            elif scan == "run":
                print("\n" + G + "Waiting Results\n" + ENDC)
                os.system("nmap -T4 -Pn --script dns-brute.nse -oN reports/dnsscanner/report.txt " + targ + " > /dev/null")
                print("\n# Sublists of " + targ)
                print("-------------------------------------------------------------")
                print("")
                os.system("cat reports/dnsscanner/report.txt | sed -n '12,100'p")
                print("")
                print("-------------------------------------------------------------")
            
            elif scan == "commands":  # Commands for this module
                print("\n# Commands For check_host")
                print ("--------------------------")
                print("set target   # Set The Url For Check")
                print("show target  # Showing Which Target Selected")
                print("back         # Back To WhiteBox Term")
                print("run          # Start Checking Host For Up or Down")
            
            elif scan == "back": # Back to whitebox term
                break

            elif scan == "clear":
                os.system("clear")

            elif scan == "exit":
                exit()
