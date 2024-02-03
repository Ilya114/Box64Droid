#!/bin/bash
clear
echo "Updating packages and installing dependencies to run installer"
echo ""
apt-get update &>/dev/null
apt-get -y --with-new-pkgs -o Dpkg::Options::="--force-confdef" upgrade &>/dev/null
apt install python --no-install-recommends -y &>/dev/null
clear
echo "Select the needed Box64Droid version to install:"
echo "1) Non-root version (Adreno 610-740, Android 12+)."
echo "2) Root version (Adreno 610-740, Android 10+)."
echo "3) VirGL version (For other GPUs, non-root phones, Android 12+)."
echo "4) Native version (Adreno 610-740, testing version, thanks JeezDisReez for his hard works)."
echo "5) Cancel the Box64Droid installation."
echo ""
read version
if [ -z $version ]
then
    echo "Empty version! Re-run installation script and choose correct version"
    rm install
    exit
elif [ $version = 1 ]
then
    curl -o non-root https://raw.githubusercontent.com/Ilya114/Box64Droid/main/installers/non-root.py && python3 non-root.py
elif [ $version = 2 ]
then
    curl -o non-root https://raw.githubusercontent.com/Ilya114/Box64Droid/main/installers/root.py && python3 root.py
elif [ $version = 3 ]
then
    curl -o non-root https://raw.githubusercontent.com/Ilya114/Box64Droid/main/installers/virgl.py && python3 virgl.py
elif [ $version = 4 ]
then
    curl -o non-root https://raw.githubusercontent.com/Ilya114/Box64Droid/main/installers/native.py && python3 native.py
elif [ $version = 5 ]
then
    rm install
    exit
else
    echo "Wrong version! Re-run installation script and choose correct version"
    rm install
    exit
fi
