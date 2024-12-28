import os
from box64droid import ver
print("Checking for Box64Droid updates...")
ver2=281224
if ver != ver2:
    print("New update available! Updating scripts...")
    os.system("wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/native/box64droid.py &>/dev/null")
    os.system("wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/native/start-box64.py &>/dev/null")
    os.system("mv box64droid.py start-box64.py $PREFIX/bin/")
    #print("Updating glibc-prefix...")
    #os.system("wget -q --show-progress https://github.com/Ilya114/Box64Droid/releases/download/alpha/glibc-prefix.tar.xz")
    #os.system("tar -xJf glibc-prefix.tar.xz -C $PREFIX/")
    #os.system("rm glibc-prefix.tar.xz")
    os.system("mkdir -p /data/data/com.termux/files/home/.shortcuts && chmod 700 -R /data/data/com.termux/files/home/.shortcuts")
    os.system("echo 'python3 $PREFIX/bin/box64droid.py --startwd' > '/data/data/com.termux/files/home/.shortcuts/Start Box64Droid'")
    os.system("echo 'wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/native/checkupdates.py -q && mv checkupdates.py $PREFIX/bin && python3 $PREFIX/bin/checkupdates.py' > '/data/data/com.termux/files/home/.shortcuts/Update Box64Droid'")
    print("Update done!")
    print("Changes (28.12.24):")
    print("- Added scripts to launch via homescreen via Termux:Widgets")
else:
    print("Updates not found, launching Box64Droid...")
os.system("sleep 2")
os.system("rm $PREFIX/bin/checkupdates.py")
if 'WD' in os.environ:
    os.system("python3 $PREFIX/bin/start-box64.py")
else:
    os.system("python3 $PREFIX/bin/box64droid.py --start")
exit()
