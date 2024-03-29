import os, shutil, time
def packages():
    os.system("pkg install x11-repo -y &>/dev/null")
    os.system("pkg install pulseaudio wget tsu xkeyboard-config termux-x11-nightly termux-am -y  &>/dev/null")
def check_prev_version():
    config = "/sdcard/Box64Droid"
    rootfs = "/data/data/com.termux/files/home/ubuntu"
    dev = "/data/data/com.termux/files/home/ubuntu/dev/urandom"
    if os.path.exists(config):
        shutil.rmtree(config)
    if os.path.exists(rootfs):
        if os.path.exists(dev):
            print("/dev not umounted correctly! Reboot device and run install script again")
            exit()
        else:
            os.system("sudo rm -r ~/ubuntu")
def install_rootfs():
    os.system("sudo mkdir ~/ubuntu")
    os.system("wget -q --show-progress https://github.com/Ilya114/Box64Droid/releases/download/stable/box64droid-rootfs-chroot.tar.xz")
    os.system("sudo tar -xJf box64droid-rootfs-chroot.tar.xz -C ~/ubuntu &>/dev/null")
    os.system("sudo mkdir ~/ubuntu/dev/shm")
    os.system("sudo chmod 1777 ~/ubuntu/dev/shm")
def scripts():
    os.system("wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/root/box64droid &>/dev/null")
    os.system("chmod +x box64droid")
    os.system("mv box64droid $PREFIX/bin/")
def clear_waste():
    os.system("rm box64droid-rootfs-chroot.tar.xz install root.py")
    os.system("clear")
def storage():
    if not os.path.exists("/data/data/com.termux/files/home/storage"):
        os.system("termux-setup-storage")
        time.sleep(2)
os.system("clear")
print(" Starting Box64Droid nstallation... Please allow storage permission!")
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
