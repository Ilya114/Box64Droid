import os, time, subprocess
exec(open('/sdcard/Box64Droid (native)/Box64Droid.conf').read())
exec(open('/sdcard/Box64Droid (native)/DXVK_D8VK_HUD.conf').read())
os.system("clear")
if 'WD' in os.environ:
    print("Welcome to Box64Droid! Select need resolution:")
    print("")
else:
    print("Select need resolution:")
print("1) 800x600 (4:3)")
print("2) 1024x768 (4:3)")
print("3) 1280x720 (16:9)")
print("4) 1920x1080 (16:9)")
print("5) Custom resolution")
if 'WD' in os.environ:
    print("6) Exit")
else:
    print("6) Back to previous menu")
print("")
res = input()
if res != "1" and res != "2" and res != "3" and res != "4" and res != "5" and res != "6" and res != "7":
    print("Incorrect or empty resolution!")
    os.system("python3 $PREFIX/bin/start-box64.py")
    exit()
elif res == "5":
    os.system("clear")
    res = input("Write need resolution: ")
    if res == "":
        print("Empty resolution!")
        os.system("python3 $PREFIX/bin/start-box64.py")
        exit()
    os.system("clear")
    print("\033[0;33mTermux-X11 and Wine started. If you want exit from Box64Droid, type \033[0;36m'1'\033[0;33m (or any key) or \033[0;36m'2'\033[0;33m to back to main menu in the terminal then press enter.\033[0m")
    os.system("taskset -c 4-7 box64 wine explorer /desktop=shell," + res + " $PREFIX/glibc/opt/autostart.bat &>/dev/null &")
elif res == "6":
    if 'WD' in os.environ:
        exit()
    else:
        os.system("python3 $PREFIX/bin/box64droid.py --start")
        exit()
else:
    os.system("clear")
    if res == "1":
        res = "800x600"
    if res == "2":
        res = "1024x768"
    if res == "3":
        res = "1280x720"
    if res == "4":
        res = "1920x1080"
    print("\033[0;33mTermux-X11 and Wine started. If you want exit from Box64Droid, type \033[0;36m'1'\033[0;33m (or any key) or \033[0;36m'2'\033[0;33m to back to main menu in the terminal then press enter.\033[0m")
    os.system("taskset -c 4-7 box64 wine explorer /desktop=shell," + res + " $PREFIX/glibc/opt/autostart.bat &>/dev/null &")
os.system("am start -n com.termux.x11/com.termux.x11.MainActivity &>/dev/null")
stop = input()
if stop == "2":
    print(" Stopping Wine...")
    os.system("box64 wineserver -k &>/dev/null")
    os.system("python3 $PREFIX/bin/box64droid.py --start")
    exit()
else:
    print(" Stopping Wine...")
    print("")
    os.system("box64 wineserver -k &>/dev/null")
    print(" Stopping Termux-X11...")
    print("")
    os.system("pkill -f pulseaudio && pkill -f 'app_process / com.termux.x11'")
    print(" Exiting from Box64Droid...")
    print("")
    exit()
