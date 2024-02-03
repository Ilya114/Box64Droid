import os, shutil, time
def packages():
    os.system("pkg install x11-repo -y &>/dev/null")
    os.system("pkg install pulseaudio wget xkeyboard-config virglrenderer-android proot-distro termux-x11-nightly termux-am -y &>/dev/null")
def check_prev_version():
    config = "/sdcard/Box64Droid"
    if os.path.exists(config):
        shutil.rmtree(config)
    os.system("proot-distro remove ubuntu-box64droid &>/dev/null")
def install_rootfs():
    os.makedirs("/data/data/com.termux/files/usr/var/lib/proot-distro", exist_ok=True)
    os.makedirs("/data/data/com.termux/files/usr/var/lib/proot-distro/installed-rootfs", exist_ok=True)
    os.makedirs("/data/data/com.termux/files/usr/var/lib/proot-distro/installed-rootfs/ubuntu", exist_ok=True)
    os.system("wget -q --show-progress https://github.com/Ilya114/Box64Droid/releases/download/stable/box64droid-rootfs-virgl.tar.xz")
    os.system("proot-distro restore box64droid-rootfs-virgl.tar.xz &>/dev/null")
def scripts():
    os.system("wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/virgl/box64droid &>/dev/null")
    os.system("wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/non-root/start-box64droid &>/dev/null")
    os.system("chmod +x start-box64droid box64droid")
    os.system("mv box64droid start-box64droid $PREFIX/bin/")
def clear_waste():
    os.system("rm box64droid-rootfs-virgl.tar.xz install virgl.py")
    os.system("clear")
def storage():
    os.system("termux-setup-storage")
    time.sleep(2)
os.system("clear")
print(" Starting Box64Droid (virgl version) installation... Please allow storage permission!")
storage()
print("")
print(" Installing packages...")
print("")
packages()
print(" Checking for older Box64Droid versions and removing them if any...")
print("")
check_prev_version()
print(" Downloading and installing rootfs, please wait...")
print("")
install_rootfs()
print("")
print(" Downloading starting scripts...")
print("")
scripts()
print(" Removing the installation waste...")
clear_waste()
print(" Installation finished. To start Box64Droid run 'box64droid --start', to see more arguments run 'box64droid --help'")
print("")
print(" And if everything goes as planned, Wine and 7-Zip file manager will start.")
print("")
