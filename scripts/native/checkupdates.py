import os
from box64droid import ver
print("Checking for Box64Droid updates...")
ver2=240230
if ver != ver2:
    print("New update available! Installing...")
    os.system("wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/native/box64droid.py &>/dev/null")
    os.system("wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/native/start-box64.py &>/dev/null")
    os.system("mv box64droid.py start-box64.py $PREFIX/bin/")
    print("Update done!")
    print("Changes:")
    print("- Added updates system")
else:
    print("Updates not found")
os.system("sleep 2")
os.system("rm $PREFIX/bin/checkupdates.py")
os.system("python3 $PREFIX/bin/box64droid.py --start")
exit()

