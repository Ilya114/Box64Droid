import os, shutil, time
def download_widget_scripts():
    os.system("mkdir -p /data/data/com.termux/files/home/.shortcuts && chmod 700 -R /data/data/com.termux/files/home/.shortcuts")
    os.system(r"wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/nativewd/1\)\ Start\ Box64Droid -q -P /data/data/com.termux/files/home/.shortcuts")
    os.system(r"wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/nativewd/2\)\ Change\ Wine\ version -q -P /data/data/com.termux/files/home/.shortcuts")
    os.system(r"wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/nativewd/3\)\ Update\ Box64Droid -q -P /data/data/com.termux/files/home/.shortcuts")
    os.system(r"wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/nativewd/4\)\ Update\ Box64 -q -P /data/data/com.termux/files/home/.shortcuts")
    os.system(r"wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/nativewd/5\)\ Open\ Winetricks -q -P /data/data/com.termux/files/home/.shortcuts")
    os.system(r"wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/nativewd/6\)\ Recreate\ Wine\ prefix -q -P /data/data/com.termux/files/home/.shortcuts")
    os.system(r"wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/nativewd/7\)\ Uninstall\ Box64Droid -q -P /data/data/com.termux/files/home/.shortcuts")
def packages():
    os.system("pkg install x11-repo glibc-repo -y &>/dev/null")
    os.system("pkg install pulseaudio wget glibc git xkeyboard-config freetype fontconfig libpng xorg-xrandr termux-x11-nightly termux-am zenity which bash curl sed cabextract -y --no-install-recommends &>/dev/null")
def check_prev_version():
    prefix = "/data/data/com.termux/files/home/.wine"
    glibc = "/data/data/com.termux/files/usr/glibc"
    config = "/sdcard/Box64Droid"
    if os.path.exists(prefix):
        shutil.rmtree(prefix)
    if os.path.exists(glibc):
        shutil.rmtree(glibc)
    if os.path.exists(config):
        shutil.rmtree(config)
def install_glibc():
    os.system("wget -q --show-progress https://github.com/Ilya114/Box64Droid/releases/download/alpha/glibc-prefix.tar.xz")
    os.system("tar -xJf glibc-prefix.tar.xz -C $PREFIX/")
def scripts():
    os.system("wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/native/box64droid &>/dev/null")
    os.system("wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/native/box64droid.py &>/dev/null")
    os.system("wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/native/start-box64.py &>/dev/null")
    os.system("wget https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks &>/dev/null")
    os.system("chmod +x box64droid winetricks")
    os.system("mv box64droid box64droid.py start-box64.py winetricks $PREFIX/bin/")
    os.system("ln -s $PREFIX/glibc/opt/wine/bin/wine $PREFIX/glibc/bin/wine")
    os.system("ln -s $PREFIX/glibc/opt/wine/bin/wine64 $PREFIX/glibc/bin/wine64")
    os.system("ln -s $PREFIX/glibc/opt/wine/bin/wineserver $PREFIX/glibc/bin/wineserver")
    os.system("ln -s $PREFIX/glibc/opt/wine/bin/wineboot $PREFIX/glibc/bin/wineboot")
    os.system("ln -s $PREFIX/glibc/opt/wine/bin/winecfg $PREFIX/glibc/bin/winecfg")
def clear_waste():
    os.system("rm glibc-prefix.tar.xz install native.py")
    os.system("clear")
def storage():
    if not os.path.exists("/data/data/com.termux/files/home/storage"):
        os.system("termux-setup-storage")
        time.sleep(2)
os.system("clear")
print(" Starting Box64Droid installation... Please allow storage permission!")
storage()
print("")
print(" Installing packages (might be long)...")
print("")
packages()
print(" Checking for older Box64Droid versions and removing them if any...")
print("")
check_prev_version()
print(" Downloading and unpacking glibc-prefix, please wait...")
print("")
install_glibc()
print("")
print(" Downloading starting scripts...")
print("")
scripts()
print("Creating scripts to launch via widget...")
download_widget_scripts()
print(" Removing the installation waste...")
clear_waste()
print(' Installation finished. To start Box64Droid create Termux:Widget widget (app should be already installed) then run "1) Start Box64Droid" or run "box64droid --start" in Termux (outdated), to see more arguments run "box64droid --help"')
print("")
print(" And if everything goes as planned, Wine and 7-Zip file manager will start.")
print("")
