import os
from box64droid import ver
print("Checking for Box64Droid updates...")
ver2=104242
if ver != ver2:
    print("New update available! Updating scripts...")
    os.system("wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/native/box64droid.py &>/dev/null")
    os.system("wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/native/start-box64.py &>/dev/null")
    os.system("mv box64droid.py start-box64.py $PREFIX/bin/")
    print("Updating glibc-prefix...")
    os.system("wget -q --show-progress https://github.com/Ilya114/Box64Droid/releases/download/alpha/glibc-prefix.tar.xz")
    os.system("tar -xJf glibc-prefix.tar.xz -C $PREFIX/")
    os.system("rm glibc-prefix.tar.xz")
    print("Update done!")
    print("Changes:")
    print("- Updated Turnip (64 bit)")
    print("- Updated Box64")
    print("- Added Wine 9.5")
else:
    print("Updates not found")
os.system("sleep 2")
os.system("rm $PREFIX/bin/checkupdates.py")
os.system("python3 $PREFIX/bin/box64droid.py --start")
exit()
