import colorama
import requests
import time
import base64
import os
from colorama import init, Fore, Back, Style
colorama.init()
os.system("clear")

command_list = "|  [1]Maskphish\n|  [2]Shodan-eye\n|  [3]Profilier\n|  [4]IPicker\n|  [I]Information\n|  [E]Exit"

print("████████╗████████╗██╗░░\n╚══██╔══╝╚══██╔══╝██║░░\n░░░██║░░░░░░██║░░░██║░░\n░░░██║░░░░░░██║░░░██║░░\n░░░██║░░░░░░██║░░░██║░░\n░░░╚═╝░░░░░░╚═╝░░░╚═╝░░\n\n" + Fore.GREEN + "This script will help you install tools in your termux!\n")

time.sleep(2)

print("Select the install tool:\n" + Fore.RED + command_list)
while True:
    choose_tool = input(Fore.GREEN + "Choose tool number: ")
    
    if choose_tool in "1":
        print(Fore.RED + "Installing Maskphish in the selected directory...")
        os.system("echo 3 | pkg install git >/dev/null 2>&1")
        os.system("echo 3 | git clone https://github.com/jaykali/maskphish >/dev/null 2>&1")
        os.chdir(os.getcwd() + "/maskphish")
        os.chmod("maskphish.sh", 509)
        print(Fore.GREEN + 'Download completed successfully! Go to the "' + Fore.RED + 'maskphish' + Fore.GREEN + '" folder and use "' + Fore.RED + './maskphish.sh' + Fore.GREEN + '" to the terminal!')
    elif choose_tool in "2":
        print(Fore.RED + "Installing Shodan-eye in the selected directory...")
        os.system("echo 3 | pkg install python3 git >/dev/null 2>&1")
        os.system("echo 3 | git clone https://github.com/BullsEye0/shodan-eye.git >/dev/null 2>&1")
        os.chdir(os.getcwd() + "/shodan-eye")
        os.system("echo 3 | pip3 install -r requirements.txt >/dev/null 2>&1")
        print(Fore.GREEN +'Download completed successfully! Go to the "' + Fore.RED + 'shodan-eye' + Fore.GREEN + '" folder and use "' + Fore.RED + 'python3 shodan-eye.py' + Fore.GREEN + '" to the terminal!')

    elif choose_tool in "3":
        print(Fore.RED + "Installing Profiler in the selected directory...")
        os.system("echo 3 | pkg install python2 git >/dev/null 2>&1")
        os.system("echo 3 | pip2 install requests >/dev/null 2>&1")
        os.system("echo 3 | git clone https://github.com/Err0r-ICA/Profiler >/dev/null 2>&1")
        print(Fore.GREEN +'Download completed successfully! Go to the "' + Fore.RED + 'Profiler' + Fore.GREEN + '" folder and use "' + Fore.RED + 'python2 Profiler' + Fore.GREEN + '" to the terminal!')

    elif choose_tool in "4":
        print(Fore.RED + "Installing IPicker in the selected directory...")
        os.system("echo 3 | pkg install python git >/dev/null 2>&1")
        os.system("echo 3 | git clone https://github.com/Deadpool2000/IPicker.git >/dev/null 2>&1")
        print(Fore.GREEN +'Download completed successfully! Go to the "' + Fore.RED + 'IPicker' + Fore.GREEN + '" folder and use "' + Fore.RED + 'python ipicker.py' + Fore.GREEN + '" to the terminal!')

    elif choose_tool in "I":
        print("\n" + Fore.GREEN + "TTI by " + Fore.RED + "Harikso" + Fore.GREEN + " - Termux Tools Installer\nVersion: " + Fore.RED + "1.0\n" + Fore.GREEN + "The first version of the script was created on 09.01.22.\nThe script was created to quickly and accurately install different tools.\nCommands:\n" + Fore.RED + command_list)

    elif choose_tool in "E":
        exit()