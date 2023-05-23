import os, time

def clear():
    os.system("clear")

def logo():
    print("             _   _                      ")
    print("            | \ | |                       ")
    print(" _ __  _   _|  \| |_ __ ___   __ _ _ __   ")
    print("| '_ \| | | | . ` | '_ ` _ \ / _` | '_ \/")
    print("| |_) | |_| | |\  | | | | | | (_| | |_) |")
    print("| .__/ \__, \_| \_/_| |_| |_|\__,_| .__/ ")
    print("| |     __/ |                     | |     ")
    print("|_|    |___/                      |_|  ")

def frame():
    print("Xx---------------------------------------xX")

clear()
frame()
print()
logo()
print()
frame()
print()
print("Welcome to pyNmap")
print()
print("1: NORMAL SCAN")
print("2: PING SCAN")
print("3: STEALTH SCAN + PROXYCHAINS (for linux only)")
print("4: ENABLE PROXYCHAINS (for linux only)")
print("5: DISABLE PROXYCHAINS (for linux only)")
print("6: INSTALL NMAP FOR (UBUNTU, KALI , PARROT, DEBIAN)")
print("7: INSTALL NMAP FOR (ARCH LINUX, MANJARO LINUX, ALL ARCH LINUX BASED OS)")
print("8: INSTALL NMAP FOR (FEDORA)")
print("9: INSTALL PROXYCHAINS FOR (UBUNTU, KALI , PARROT, DEBIAN)")
print("10: INSTALL PROXYCHAINS FOR (ARCH LINUX, MANJARO LINUX, ALL ARCH LINUX BASED OS)")
print("11: INSTALL PROXYCHAINS FOR (FEDORA)")
print("12: TCP SCAN")
print()
command = input("$ ")

if command == "1":
    clear()
    target = input("target: ")
    os.system("sudo nmap " + target)
    time.sleep(10)
    os.system("python3 pymap.py")


if command == "2":
    clear()
    target = input("target: ")
    os.system("sudo nmap -sP " + target)
    time.sleep(10)
    os.system("python3 pymap.py")    

if command == "3":
    clear()
    target = input("target: ")
    os.system("sudo proxychains nmap -sS" + target)
    time.sleep(10)
    os.system("python3 pymap.py")    

if command == "4":
    clear()
    os.system("sudo service tor start")
    time.sleep(0.5)
    os.system("python3 pymap.py")      

if command == "5":
    clear()
    os.system("sudo service tor stop")
    time.sleep(0.5)
    os.system("python3 pymap.py")      

if command == "6":
    clear()
    os.system("sudo apt update")
    os.system("sudo apt install nmap -y")
    time.sleep(0.5)
    os.system("python3 pymap.py")       

if command == "7":
    clear()
    os.system("sudo pacman -S nmap -y")
    time.sleep(0.5)
    os.system("python3 pymap.py")     

if command == "8":
    clear()
    os.system("sudo dnf update")
    os.system("sudo dnf install nmap -y")
    time.sleep(0.5)
    os.system("python3 pymap.py")

if command == "9":
    clear()
    os.system("sudo apt update")
    os.system("sudo apt install proxychains tor -y")
    time.sleep(0.5)
    os.system("python3 pymap.py")       

if command == "10":
    clear()
    os.system("sudo pacman -S proxychains tor -y")
    time.sleep(0.5)
    os.system("python3 pymap.py")     

if command == "11":
    clear()
    os.system("sudo dnf update")
    os.system("sudo dnf install proxychains tor -y")
    time.sleep(0.5)
    os.system("python3 pymap.py")
if command == "12":
    clear()
    target = input("target: ")
    os.system("sudo nmap -sT " + target)
    time.sleep(10)
    os.system("python3 pymap.py")          
 