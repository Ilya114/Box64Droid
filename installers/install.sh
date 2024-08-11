#!/bin/bash
clear
echo "Updating packages and installing dependencies to run installer"
echo ""
apt-get update &>/dev/null
apt-get -y --with-new-pkgs -o Dpkg::Options::="--force-confdef" upgrade &>/dev/null
apt install python --no-install-recommends -y &>/dev/null
clear
echo "Hello, this is a Box64Droid installer, please select need version to install:"
echo ""
echo "Actual version:"
echo "1) Native (Adreno 610-750, Android 10+)"
echo ""
echo "Irrelevant versions:"
echo "2) Non-root (Adreno 610-750, Android 12+)"
echo "3) Root (Adreno 610-750, Android 10+)"
echo "4) VirGL (Other GPU's, based on non-root, Android 12+)"
echo ""
echo "5) Cancel the Box64Droid installation"
echo ""
read version
if [ -z $version ]
then
    echo "Empty version! Re-run installation script and choose correct version"
    rm install
    exit
elif [ $version = 1 ]
then
    curl -o native.py https://raw.githubusercontent.com/Ilya114/Box64Droid/main/installers/native.py && python3 native.py
elif [ $version = 2 ]
then
    curl -o non-root.py https://raw.githubusercontent.com/Ilya114/Box64Droid/main/installers/non-root.py && python3 non-root.py
elif [ $version = 3 ]
then
    curl -o root.py https://raw.githubusercontent.com/Ilya114/Box64Droid/main/installers/root.py && python3 root.py
elif [ $version = 4 ]
then
    curl -o virgl.py https://raw.githubusercontent.com/Ilya114/Box64Droid/main/installers/virgl.py && python3 virgl.py
elif [ $version = 5 ]
then
    rm install
    exit
else
    echo "Wrong version! Re-run installation script and choose correct version"
    rm install
    exit
fi
