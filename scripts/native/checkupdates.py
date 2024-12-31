import os
from box64droid import ver
print("Checking for Box64Droid updates...")
ver2=311224
if ver != ver2:
    print("New update available! Updating scripts...")
    os.system("wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/native/box64droid.py &>/dev/null")
    os.system("wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/native/start-box64.py &>/dev/null")
    os.system("mv box64droid.py start-box64.py $PREFIX/bin/")
    os.system("rm $HOME/.shortcuts/*")
    os.system("wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/nativewd/1\)\ Start\ Box64Droid -q -P /data/data/com.termux/files/home/.shortcuts")
    os.system("wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/nativewd/2\)\ Change\ Wine\ version -q -P /data/data/com.termux/files/home/.shortcuts")
    os.system("wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/nativewd/3\)\ Update\ Box64Droid -q -P /data/data/com.termux/files/home/.shortcuts")
    os.system("wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/nativewd/4\)\ Update\ Box64 -q -P /data/data/com.termux/files/home/.shortcuts")
    os.system("wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/nativewd/5\)\ Open\ Winetricks -q -P /data/data/com.termux/files/home/.shortcuts")
    os.system("wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/nativewd/6\)\ Recreate\ Wine\ prefix -q -P /data/data/com.termux/files/home/.shortcuts")
    os.system("wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/nativewd/7\)\ Uninstall\ Box64Droid -q -P /data/data/com.termux/files/home/.shortcuts")
    print("Updating glibc-prefix...")
    os.system("wget -q --show-progress https://github.com/Ilya114/Box64Droid/releases/download/alpha/glibc-prefix.tar.xz")
    os.system("tar -xJf glibc-prefix.tar.xz -C $PREFIX/")
    os.system("rm glibc-prefix.tar.xz")
    print("Update done!")
    print("Changes (31.12.24):")
    print("- Now Box64Droid can be fully used via Termux:Widget")
    print("- Updated Box64")
    print("- Updated Mesa Turnip to 25.0.0-devel (thanks KIMCHI for build)")
    print("- Added DXVK 2.5.2 and DXVK-GPLAsync 2.5.1 (as Async)")
    print("- Added WineD3D 9.0")
    print("- Renamed folders and some shortcuts in Wine start menu")
else:
    print("Updates not found, launching Box64Droid...")
os.system("sleep 2")
os.system("rm $PREFIX/bin/checkupdates.py")
if 'WD' in os.environ:
    os.system("python3 $PREFIX/bin/start-box64.py")
else:
    os.system("python3 $PREFIX/bin/box64droid.py --start")
exit()
