#!/usr/bin/env python3

import os
import sys
import click
from tqdm import tqdm
from time import sleep

# Exception Handling for First Argument
try:
    url = sys.argv[1]
except:
    os.system("echo '\033[1mYou forgot the \"url\" argument... Please run the program like the example below: \033[0m'")
    os.system("echo 'python assetfinder.py example.com'")
    sys.exit(1)

# ARRRRTTTTTT
width = os.get_terminal_size().columns

print("""
\033[1;38;2;250;250;110m    _   ___ ___ ___ _____   ___ ___ _  _ ___  ___ ___  \033[0m
\033[1;38;2;170;228;121m   /_\ / __/ __| __|_   _| | __|_ _| \| |   \| __| _ \ \033[0m
\033[1;38;2;100;201;135m  / _ \\\__ \__ \ _|  | |   | _| | || .` | |) | _||   / \033[0m
\033[1;38;2;35;170;143m /_/ \_\___/___/___|_|_|   |_| |___|_|\_|___/|___|_|_\ \033[0m
\033[1;38;2;0;137;138m            | || | __| |  | _ \ __| _ \ |              \033[0m
\033[1;38;2;23;104;119m            | __ | _|| |__|  _/ _||   /_|              \033[0m
\033[1;38;2;42;72;88m            |_||_|___|____|_| |___|_|_(_)              
\033[0m
\033[1mA Tool To Help Automate AssetFinder, Created By TomNomNom ➡️  (github.com/tomnomnom)
""")
sleep(1)

#Code For Execution
for char in tqdm(["a", "b", "c", "d", "e", "f", "g", "h"], desc="Overall Progress", position=0, colour="green", dynamic_ncols=True):
    while char == "a":
        sleep(0.75)
        tqdm.write("\nStarting The Process For " + url.upper() + "!")
        sleep(1)
        char += char
    while char == "b":
        sleep(0.25)
        tqdm.write("1️⃣  Verifying The \"URL\" Folder Exists")
        sleep(0.25)
        if not os.path.exists(url):
            os.mkdir(url)
        tqdm.write("Finished Verification, Moving On")
        sleep(0.25)
        char += char
    while char == "c":
        tqdm.write("2️⃣  Verifying The \"Recon\" Folder Exists")
        sleep(0.25)
        if not os.path.exists(url + "/recon"):
            os.mkdir(url + "/recon")
        tqdm.write("Finished Verification, Moving On")
        sleep(0.25)
        char += char
    while char == "d":
        tqdm.write("3️⃣  Creating A File Named \"Assets.txt\"")
        sleep(0.25)
        open(url + "/recon/assets.txt", "w+")
        tqdm.write("Finished Creating File, Moving On")
        sleep(0.25)
        char += char
    while char == "e":
        tqdm.write("4️⃣  Running Assetfinder By TomNomNom For " + url.upper() + " & Placing Results Into Assets.txt")
        sleep(0.25)
        os.system('assetfinder ' + url + ' >> ' + url + '/recon/assets.txt')
        tqdm.write("Finished Running Assetfinder, Moving On")
        sleep(0.25)
        char += char
    while char == "f":
        tqdm.write("5️⃣  Opening Assets.txt File For Reading & Transferring Results From Assetfinder To Final.txt File")
        sleep(0.25)
        with open(url + '/recon/assets.txt') as f:
            lines = f.readlines()
        tqdm.write("Finished Opening Assets.txt For Reading, Moving On")
        sleep(0.25)
        char += char
    while char == "g":
        tqdm.write("6️⃣  Transferring Results From Assets.txt To Final.txt (i.e. Getting Rid of Duplicates & Any Result Without " + url.upper() + ")")
        sleep(0.25)
        with open(url + '/recon/final.txt', 'w') as f:
            for line in lines:
                if url in line:
                    f.write(line)
        tqdm.write("Finished Transferring Results, Moving On")
        sleep(0.25)
        char += char
    while char == "h":
        sleep(0.75)
        tqdm.write("7️⃣  Cleaning Everything Up")
        sleep(0.5)
        tqdm.write("Finished Running The Program!")
        sleep(0.75)
        char += char
print("\nQuestion [In Dwight Schrute's Voice]... Would You Like To Delete The Assets.txt File & Just Keep The Final.txt File? Blank = Yes")
if (click.confirm("", default=True)):
    os.remove(url + '/recon/assets.txt')
    os.system("echo '\nRemoved Assets.txt!'")
    sleep(0.25)
    os.system("echo 'Done! Buh-Bye 👋'")
    sleep(0.25)
else:
    sleep(0.25)
    os.system("echo '\nDone! Buh-Bye 👋'")
    sleep(0.25)
