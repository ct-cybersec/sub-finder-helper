#!/usr/bin/env python3
# SCRIPT WITH PROGRESS BAR!!!

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
\033[1;38;2;250;250;110m  ___ _   _ ___   ___ ___ _  _ ___  ___ ___ \033[0m
\033[1;38;2;170;228;121m / __| | | | _ ) | __|_ _| \| |   \| __| _ \\\033[0m
\033[1;38;2;100;201;135m \__ \ |_| | _ \ | _| | || .` | |) | _||   /\033[0m
\033[1;38;2;35;170;143m |___/\___/|___/_|_| |___|_|\_|___/|___|_|_\\\033[0m
\033[1;38;2;0;137;138m        | || | __| |  | _ \ __| _ \ |       \033[0m
\033[1;38;2;23;104;119m        | __ | _|| |__|  _/ _||   /_|       \033[0m
\033[1;38;2;42;72;88m        |_||_|___|____|_| |___|_|_(_)                     
\033[0m
\033[1mAn Automation Tool To Help Discover Subdomains,\n       Check Alive Subdomains, & More!\n\n          Created By: ct-cybersec\033[0m
""")
sleep(1)

# This Is The Status Bar - Updates After Iteration Through The Given Range. The Sleeps Aren't Really Necessary, But It Makes It Nicer-Looking
for char in tqdm(range(1, 101, 1), colour = "green", position = 1, leave = False, mininterval = 0.01, smoothing = 1, desc = "Overall Progress: ", bar_format = "{desc:}{percentage:.0f}%|{bar}{r_bar}"):
    if char == 1:
        tqdm.write("\n\033[1;38;2;250;250;110mStarting The Process For " + url.upper() + "!\033[0m")
    if (char <= 8 and char > 1):
        sleep(0.05)
    if char == 9:
        # Creating A Directory That Is Labelled As The Url You, The User, Has Put As The Argument
        tqdm.write("\033[1;38;2;209;240;114m(1) Verifying The \"URL\" Folder Exists\033[0m")
        if not os.path.exists(url):
            os.mkdir(url)
        tqdm.write("\033[1;38;2;209;240;114mFinished Verification, Moving On\033[0m")
    if (char <= 18 and char > 9):
        sleep(0.05)
    if char == 19:
        # Creating A Directory That Is Labelled "Recon" Inside The URL Folder
        tqdm.write("\033[1;38;2;170;228;121m(2) Verifying The \"Recon\" Folder Exists\033[0m")
        if not os.path.exists(url + "/recon"):
            os.mkdir(url + "/recon")
        tqdm.write("\033[1;38;2;170;228;121mFinished Verification, Moving On\033[0m")
    if (char <= 27 and char > 19):
        sleep(0.05)
    if char == 28:
        # Creating & Opening A File Named "Assets.txt" For Later Use
        tqdm.write("\033[1;38;2;134;215;128m(3) Creating A File Named \"Assets.txt\" & \"Amass.txt\"\033[0m")
        open(url + "/recon/assets.txt", "w+")
        open(url + "/recon/amass.txt", "w+")
        tqdm.write("\033[1;38;2;134;215;128mFinished Creating Files, Moving On\033[0m")
    if (char <= 36 and char > 28):
        sleep(0.05)
    if char == 37:
        # Running Assetfinder, Created By TomNomNom, Using The URL Supplied & Placing Results Into The "Assets.txt" File
        tqdm.write("\033[1;38;2;100;201;135m(4) Running Assetfinder By TomNomNom For " + url.upper() + " & Placing Results Into \"Assets.txt\"\033[0m")
        os.system("assetfinder " + url + " >> " + url + "/recon/assets.txt")
        tqdm.write("\033[1;38;2;100;201;135mFinished Running Assetfinder, Moving On\033[0m")
    if (char <= 45 and char > 37):
        sleep(0.05)
    if char == 46:
        # Running Amass Using The URL Supplied & Placing Results Into The "Amass.txt" File
        tqdm.write("\033[1;38;2;68;185;141m(5) Running Amass For " + url.upper() + " & Placing Results Into \"Amass.txt\"\nNOTE: Be Patient, Amass Takes A While!\033[0m")
        os.system("amass enum -silent -o " + url + "/recon/amass.txt -d " + url)
        tqdm.write("\033[1;38;2;68;185;141mFinished Running Amass, Moving On\033[0m")
    if (char <= 54 and char > 46):
        sleep(0.05)
    if char == 55:
        # Reading "Assets.txt" File To Transfer Non-Duplicates & Results That Contain The URL Given
        tqdm.write("\033[1;38;2;35;170;143m(6) Opening \"Assets.txt\" & \"Amass.txt\" Files For Reading\033[0m")
        with open(url + "/recon/assets.txt", "r") as f, open(url + "/recon/amass.txt", "r") as f2:
            asset_lines = f.readlines()
            amass_lines = f2.readlines()
        asset_lines_set = set(asset_lines)
        amass_lines_set = set(amass_lines) 
        tqdm.write("\033[1;38;2;35;170;143mFinished Opening Files For Reading, Moving On\033[0m")
    if (char <= 63 and char > 55):
        sleep(0.05)
    if char == 64:
        # Transferring The Above URL Results To Their Respective Final Results File
        tqdm.write("\033[1;38;2;0;153;143m(7) Transferring Results From Initial Results To Final Results (i.e. Getting Rid of Duplicates & Any Result Without " + url.upper() + ")\033[0m")
        with open(url + "/recon/assets_final.txt", "w") as f, open(url + "/recon/amass_final.txt", "w") as f2:
            for asset_new_line in asset_lines_set:
                if url in asset_new_line:
                    f.write(asset_new_line)
            for amass_new_line in amass_lines_set:
                if url in amass_new_line:
                    f2.write(amass_new_line)  
        tqdm.write("\033[1;38;2;0;153;143mFinished Transferring Results, Moving On\033[0m")
    if (char <= 72 and char > 64):
        sleep(0.05)
    if char == 73:
        # Creating A Directory Called "HTTProbe" for HTTProbe Results
        tqdm.write("\033[1;38;2;0;137;138m(8) Verifying The \"HTTProbe\" Folder Exists\033[0m")        
        if not os.path.exists(url + "/recon/httprobe"):
            os.mkdir(url + "/recon/httprobe")
        tqdm.write("\033[1;38;2;0;137;138mFinished Verification, Moving On\033[0m")
    if (char <= 81 and char > 73):
        sleep(0.05)
    if char == 82:
        # Running HTTProbe To Check For Live Domains By Reading (Cat) The Two Result Files
        tqdm.write("\033[1;38;2;0;120;130m(9) Running HTTProbe To Check For Live Domains & Placing Results Into Their Respective \"Alive\" Files\033[0m")
        os.system("cat " + url + "/recon/assets_final.txt | sort -u | sed \'s/https\?:\/\///\' | sed \'s/http\?:\/\///\' | tr -d \':443\' | tr -d \':80\' >> " + url + "/recon/httprobe/a1.txt")
        os.system("cat " + url + "/recon/amass_final.txt | sort -u | sed \'s/https\?:\/\///\' | sed \'s/http\?:\/\///\' | tr -d \':443\' | tr -d \':80\' >> " + url + "/recon/httprobe/a2.txt")
        os.system("sort -u " + url + "/recon/httprobe/a1.txt > " + url + "/recon/httprobe/alive_assets.txt")
        os.system("sort -u " + url + "/recon/httprobe/a2.txt > " + url + "/recon/httprobe/alive_amass.txt")
        os.system("rm " + url + "/recon/httprobe/a1.txt")
        os.system("rm " + url + "/recon/httprobe/a2.txt")
        tqdm.write("\033[1;38;2;0;120;130mFinished Running HTTProbe, Moving On\033[0m")
    if (char <= 90 and char > 82):
        sleep(0.05)
    if char == 91:
        # Reading & Transferring The Two Alive Files To A Combined Alive File
        tqdm.write("\033[1;38;2;0;120;130m(10) Transferring Alive Results To A Combined File\033[0m")
        files = (url + "/recon/httprobe/alive_assets.txt", url + "/recon/httprobe/alive_amass.txt")
        all_lines = []
        for f in files:
            with open(f,"r") as fi:
                all_lines += fi.readlines()
        all_lines = set(all_lines)
        with open(url + "/recon/httprobe/alive_combined.txt", "w") as fo:
            fo.write("".join(all_lines))
        tqdm.write("\033[1;38;2;0;120;130mFinished Combining Alive Results, Moving On\033[0m")
    if (char <= 99 and char > 91):
        sleep(0.05)               
    if char == 100:
        tqdm.write("\033[1;38;2;23;104;119mCleaning Everything Up\033[0m")
        sleep(0.05)
        tqdm.write("\033[1;38;2;23;104;119mFinished Running The Program!\033[0m")
        sleep(1)
# Using Click Library, Asking If You, The User, Want To Delete The Original Result Files Or Keep Them
tqdm.write("\nQuestion [In Dwight Schrute's Voice]: Would You Like To Delete The Original \"Assets.txt\" & \"Amass.txt\" Files (Keeping Final Files)? Blank = Yes\033[0m")
if (click.confirm("", default=True)):
    os.remove(url + "/recon/assets.txt")
    os.remove(url + "/recon/amass.txt")
    os.system("echo '\nRemoved Assets.txt & Amass.txt & Kept The Final Files!\033[0m'")
    os.system("echo 'Continuing On...\033[0m'")
else:
    os.system("echo 'Continuing On...\033[0m'")
sleep(0.5)
tqdm.write("\nLast Question: Would You Like To Delete The Original Alive Files (Keeping Combined)? Blank = Yes\033[0m")
# Using Click Library, Asking If You, The User, Want To Delete The Original Alive Files Or Keep Them
if (click.confirm("", default=True)):
    os.remove(url + "/recon/httprobe/alive_assets.txt")
    os.remove(url + "/recon/httprobe/alive_amass.txt")
    os.system("echo '\nRemoved Original Alive Files & Kept The Combined File!\033[0m'")
    os.system("echo 'Done! Buh-Bye 👋\033[0m'")
else:
    os.system("echo '\nDone! Buh-Bye 👋\033[0m'")
