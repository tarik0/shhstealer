import os
import sys

print("Setup for ssh_stealer.py (Python 2x)")
print("")
print ("Downloading colorama,pyfiglet,termcolor for ASCII Banner:")
print ("")
print ("")
os.system('pip install git+https://github.com/pwaller/pyfiglet')
os.system('pip install termcolor')
os.system('pip install colorama')
print("")
print ("Downloading pexpect for SSH connection:")
print("")
print("")
os.system('pip install pexpect')
print("")
print ("Success!Now you can open the program.")


