#!/usr/bin/env python3

import os
import sys
import click
from tqdm import tqdm
from time import sleep

# Exception Handling for First Argument, Which Needs To Be A URL
try:
    url = sys.argv[1]
except:
    os.system("echo '\033[1;38;2;255;0;0mYou forgot the URL argument... Please run the program like the example below: \033[0m\npython assetfinder.py ct-cybersec.com'")
    sys.exit(1)

# Make Sure To Use The Correct URL Formatting For URL Argument. This If Statement Also Disallows A Second Argument. Will Add Special Characters Later
if (url.startswith(".")) | (url.endswith(".")):
    os.system("echo '\033[1;38;2;255;0;0mPlease use the correct scheme for a URL (i.e. ct-cybersec.com)\033[0m'")
    sys.exit(1)

# ARRRRTTTTTT
print("""
\033[1;38;2;250;250;110m    _   ___ ___ ___ _____   ___ ___ _  _ ___  ___ ___  \033[0m
\033[1;38;2;170;228;121m   /_\ / __/ __| __|_   _| | __|_ _| \| |   \| __| _ \ \033[0m
\033[1;38;2;100;201;135m  / _ \\\__ \__ \ _|  | |   | _| | || .` | |) | _||   / \033[0m
\033[1;38;2;35;170;143m /_/ \_\___/___/___|_|_|   |_| |___|_|\_|___/|___|_|_\ \033[0m
\033[1;38;2;0;137;138m            | || | __| |  | _ \ __| _ \ |              \033[0m
\033[1;38;2;23;104;119m            | __ | _|| |__|  _/ _||   /_|              \033[0m
\033[1;38;2;42;72;88m            |_||_|___|____|_| |___|_|_(_)              
\033[0m
\033[1m          A Tool To Help Automate AssetFinder\n   [Created By TomNomNom ➡️  (github.com/tomnomnom)]\033[0m
""")
sleep(1)

# This Is The Status Bar - Updates After Iteration Through The Given Range. The Sleeps Aren't Really Necessary, But It Makes It Nicer-Looking
for char in tqdm(range(1, 101, 1), colour = "green", position = 1, leave = False, mininterval = 0.01, smoothing = 1, desc = "Overall Progress: ", bar_format = "{desc:}{percentage:.0f}%|{bar}{r_bar}"):
    if char == 1:
        tqdm.write("\n\033[1;38;2;250;250;110mStarting The Process For " + url.upper() + "!\033[0m")
    if char <= 14:
        sleep(0.01)
    if char == 15:
        tqdm.write("\033[1;38;2;196;236;116m(1) Verifying The \"URL\" Folder Exists\033[0m")
        # Creating A Directory That Is Labelled As The Url You, The User, Has Put As The Argument
        if not os.path.exists(url):
            os.mkdir(url)
        tqdm.write("\033[1;38;2;196;236;116mFinished Verification, Moving On\033[0m")
    if char <= 30:
        sleep(0.01)
    if char == 31:
        tqdm.write("\033[1;38;2;146;220;126m(2) Verifying The \"Recon\" Folder Exists\033[0m")
        # Creating A Directory That Is Labelled "Recon" Inside The URL Folder
        if not os.path.exists(url + "/recon"):
            os.mkdir(url + "/recon")
        tqdm.write("\033[1;38;2;146;220;126mFinished Verification, Moving On\033[0m")
    if char <= 45:
        sleep(0.01)
    if char == 46:
        tqdm.write("\033[1;38;2;100;201;135m(3) Creating A File Named \"Assets.txt\"\033[0m")
        # Creating & Opening A File Named "Assets.txt" For Later Use
        open(url + "/recon/assets.txt", "w+")
        tqdm.write("\033[1;38;2;100;201;135mFinished Creating File, Moving On\033[0m")
    if char <= 60:
        sleep(0.01)
    if char == 61:
        tqdm.write("\033[1;38;2;57;180;142m(4) Running Assetfinder By TomNomNom For " + url.upper() + " & Placing Results Into \"Assets.txt\"\033[0m")
        # Running Assetfinder, Created By TomNomNom, Using The URL Supplied & Placing Results Into The "Assets.txt" File
        os.system('assetfinder ' + url + ' >> ' + url + '/recon/assets.txt')
        tqdm.write("\033[1;38;2;57;180;142mFinished Running Assetfinder, Moving On\033[0m")
    if char <= 75:
        sleep(0.01)
    if char == 76:
        tqdm.write("\033[1;38;2;8;159;143m(5) Opening \"Assets.txt\" File For Reading\033[0m")
        # Reading "Assets.txt" File To Transfer Non-Duplicates & Results That Contain The URL Given
        with open(url + '/recon/assets.txt', 'r') as f:
            lines = f.readlines()
        lines_set = set(lines)
        tqdm.write("\033[1;38;2;8;159;143mFinished Opening \"Assets.txt\" For Reading, Moving On\033[0m")
    if char <= 90:
        sleep(0.01)
    if char == 91:
        tqdm.write("\033[1;38;2;0;137;138m(6) Transferring Results From \"Assets.txt\" To \"Final.txt\" (i.e. Getting Rid of Duplicates & Any Result Without " + url.upper() + ")\033[0m")
        # Transferring The Above URL Results To "Final.txt" File
        with open(url + '/recon/final.txt', 'w') as f:
            for new_line in lines_set:
                f.write(new_line)
        tqdm.write("\033[1;38;2;0;137;138mFinished Transferring Results, Moving On\033[0m")
    if char <= 99:
        sleep(0.01)
    if char == 100:
        tqdm.write("\033[1;38;2;8;115;127m(7) Cleaning Everything Up\033[0m")
        sleep(0.02)
        tqdm.write("\033[1;38;2;8;115;127mFinished Running The Program!\033[0m")
        sleep(0.01)
    if char == 100:
        sleep(1)
tqdm.write("\nQuestion [In Dwight Schrute's Voice]... Would You Like To Delete The \"Assets.txt\" File & Just Keep The \"Final.txt\" File? Blank = Yes\033[0m")
# Using Click Library, Asking If You, The User, Want To Delete The Original "Assets.txt" File Or Keep It
if (click.confirm("", default=True)):
    os.remove(url + '/recon/assets.txt')
    os.system("echo '\nRemoved Assets.txt!\033[0m'")
    sleep(0.1)
    os.system("echo 'Done! Buh-Bye 👋\033[0m'")
    sleep(0.1)
else:
    os.system("echo '\nDone! Buh-Bye 👋\033[0m'")
    sleep(0.1)
