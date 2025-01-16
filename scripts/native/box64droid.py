import os, time, shutil, sys
ver=311224
def start_box64droid():
    os.system("clear")
    if "LD_PRELOAD" in os.environ:
        del os.environ["LD_PRELOAD"]
    print("Starting Termux-X11...")
    os.system("termux-x11 :0 &>/dev/null &")
    print("Starting PulseAudio...")
    os.system('pulseaudio --start --load="module-native-protocol-tcp auth-ip-acl=127.0.0.1 auth-anonymous=1" --exit-idle-time=-1 &>/dev/null')
def check_config():
    config_folder = "/sdcard/Box64Droid (native)/"
    box64droid_config = config_folder + "Box64Droid.conf"
    dxvk_config = config_folder + "DXVK_D8VK.conf"
    dxvk_config_hud =  config_folder + "DXVK_D8VK_HUD.conf"
    print("Checking configuration...")
    if not os.path.exists(config_folder):
        os.mkdir(config_folder)
    if not os.path.exists(box64droid_config):
        shutil.copyfile("/data/data/com.termux/files/usr/glibc/opt/Box64Droid.conf", box64droid_config)
    if not os.path.exists(dxvk_config):
        shutil.copyfile("/data/data/com.termux/files/usr/glibc/opt/DXVK_D8VK.conf", dxvk_config)
    if not os.path.exists(dxvk_config_hud):
        shutil.copyfile("/data/data/com.termux/files/usr/glibc/opt/DXVK_D8VK_HUD.conf", dxvk_config_hud)
    exec(open('/sdcard/Box64Droid (native)/Box64Droid.conf').read())
    exec(open('/sdcard/Box64Droid (native)/DXVK_D8VK_HUD.conf').read())
def check_prefix():
    if not os.path.exists("/data/data/com.termux/files/home/.wine"):
        print("Wine prefix not found! Creating...")
        create_prefix()
def recreate_prefix():
    prefix_path="/data/data/com.termux/files/home/.wine"
    os.system("clear")
    print("Removing previous Wine prefix...")
    shutil.rmtree(prefix_path)
    print("Creating Wine prefix...")
    create_prefix()
def create_prefix():
    os.system('WINEDLLOVERRIDES="mscoree=" box64 wineboot &>/dev/null')
    os.system('cp -r $PREFIX/glibc/opt/Shortcuts/* "$HOME/.wine/drive_c/ProgramData/Microsoft/Windows/Start Menu"')
    os.system("rm $HOME/.wine/dosdevices/z: && rm $HOME/.wine/dosdevices/d: &>/dev/null")
    os.system("ln -s /sdcard/Download $HOME/.wine/dosdevices/d: &>/dev/null && ln -s /sdcard $HOME/.wine/dosdevices/e: &>/dev/null && ln -s /data/data/com.termux/files $HOME/.wine/dosdevices/z:")
    print("Installing DXVK, D8VK and vkd3d-proton...")
    os.system(r'box64 wine "$PREFIX/glibc/opt/Resources64/Run if you will install on top of WineD3D.bat" &>/dev/null && box64 wine "$PREFIX/glibc/opt/Resources64/DXVK2.3/DXVK2.3.bat" &>/dev/null')
    os.system(r'box64 wine reg add "HKEY_CURRENT_USER\Software\Wine\DllOverrides" /v d3d12 /d native /f &>/dev/null && box64 wine reg add "HKEY_CURRENT_USER\Software\Wine\DllOverrides" /v d3d12core /d native /f &>/dev/null')
    os.system("cp $PREFIX/glibc/opt/Resources/vkd3d-proton/* $HOME/.wine/drive_c/windows/syswow64 && cp $PREFIX/glibc/opt/Resources64/vkd3d-proton/* $HOME/.wine/drive_c/windows/system32")
    print("Done!")
def change_wine_version():
    os.system("clear")
    print("Select Wine (WoW64) version to install:")
    print("1) Wine 9.1")
    print("2) Wine 9.2")
    print("3) Wine 9.4")
    print("4) Wine 9.7")
    print("5) Wine 9.11")
    print("6) Wine 9.13")
    if 'WD' in os.environ:
        print("7) Exit")
    else:
        print("7) Back to previous menu")
    print("")
    choice = input()
    if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7":
        print("Incorrect or empty option!")
        change_wine_version()
    elif choice == "7":
        if 'WD' in os.environ:
            exit()
        else:
            main_menu()
    else:
        os.system("clear")
        print("Removing previous Wine version...")
        if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine"):
            shutil.rmtree("/data/data/com.termux/files/usr/glibc/opt/wine")
        if choice == "1":
            print("Downloading Wine 9.1 (WoW64)...")
            print("")
            os.system("wget -q --show-progress https://github.com/Ilya114/Box64Droid/releases/download/alpha/wine-9.1-esync.tar.xz")
            print("")
            print("Unpacking Wine 9.1...")
            os.system("tar -xf wine-9.1-esync.tar.xz -C $PREFIX/glibc/opt")
        elif choice == "2":
            print("Downloading Wine 9.2 (WoW64)...")
            print("")
            os.system("wget -q --show-progress https://github.com/Ilya114/Box64Droid/releases/download/alpha/wine-9.2-amd64-wow64.tar.xz")
            print("")
            print("Unpacking Wine 9.2 (WoW64)...")
            os.system("tar -xf wine-9.2-amd64-wow64.tar.xz -C $PREFIX/glibc/opt")
        elif choice == "3":
            print("Downloading Wine 9.4 (WoW64)...")
            print("")
            os.system("wget -q --show-progress https://github.com/Ilya114/Box64Droid/releases/download/alpha/wine-9.4-amd64-wow64.tar.xz")
            print("")
            print("Unpacking Wine 9.4 (WoW64)...")
            os.system("tar -xf wine-9.4-amd64-wow64.tar.xz -C $PREFIX/glibc/opt")
        elif choice == "4":
            print("Downloading Wine 9.7 (WoW64)...")
            print("")
            os.system("wget -q --show-progress https://github.com/Ilya114/Box64Droid/releases/download/alpha/wine-9.7-glibc-wow64.tar.xz")
            print("")
            print("Unpacking Wine 9.7 (WoW64)...")
            os.system("tar -xf wine-9.7-glibc-wow64.tar.xz -C $PREFIX/glibc/opt")
            os.system("mv $PREFIX/glibc/opt/wine-git-166895a-exp-wow64-amd64 $PREFIX/glibc/opt/wine")
        elif choice == "5":
            print("Downloading Wine 9.11 (WoW64)...")
            print("")
            os.system("wget -q --show-progress https://github.com/Ilya114/Box64Droid/releases/download/alpha/wine-9.11-amd64-wow64.tar.xz")
            print("")
            print("Unpacking Wine 9.11 (WoW64)...")
            os.system("tar -xf wine-9.11-glibc-amd64-wow64.tar.xz -C $PREFIX/glibc/opt")
            os.system("mv $PREFIX/glibc/opt/wine-git-63e25f9-exp-wow64-amd64 $PREFIX/glibc/opt/wine")
        elif choice == "6":
            print("Downloading Wine 9.13 (WoW64)...")
            print("")
            os.system("wget -q --show-progress https://github.com/Ilya114/Box64Droid/releases/download/alpha/wine-9.13-glibc-amd64-wow64.tar.xz")
            print("")
            print("Unpacking Wine 9.13 (WoW64)...")
            os.system("tar -xf wine-9.13-glibc-amd64-wow64.tar.xz -C $PREFIX/glibc/opt")
            os.system("mv $PREFIX/glibc/opt/wine-git-8d25995-exp-wow64-amd64 $PREFIX/glibc/opt/wine")
        os.system("rm wine*")
        print("Done!")
def main_menu():
    os.system("clear")
    print("Welcome to Box64Droid! Select to start:")
    print("")
    print("1) Wine")
    print("2) Wine (debug version)")
    print("3) Change Wine version")
    print("4) Recreate Wine prefix")
    print("5) Check for updates")
    print("6) Update Box64")
    print("7) Winetricks")
    print("8) Exit")
    print("")
    print("Note: Console UI will be EOL on 1 June of 2025. ATM Box64Droid will use Termux:Widgets. To use it install and create Termux widget in homescreen") 
    print("")
    choice = input()
    if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8":
        print("Incorrect or empty option!")
        main_menu()
    elif choice == "1":
        os.system("python3 $PREFIX/bin/start-box64.py")
        exit()
    elif choice == "2":
        os.system("clear")
        print("Wine will be started with debug info, log will be saved in /sdcard/Box64Droid.log. Send /sdcard/Box64Droid.log in Telegram group if you have black screen or crashed apps/games")
        print("To exit from Box64Droid press type '1' (or any key) or '2' to back to main menu then press Enter")
        os.system("BOX86_LOG=1 BOX86_SHOWSEGV=1 BOX86_DYNAREC_LOG=1 BOX86_DYNAREC_MISSING=1 BOX86_DLSYM_ERROR=1 BOX64_LOG=1 BOX64_SHOWSEGV=1 BOX64_DYNAREC_LOG=1 BOX64_DYNAREC_MISSING=1 BOX64_DLSYM_ERROR=1 WINEDEBUG=+err taskset -c 4-7 box64 wine explorer /desktop=shell,800x600 $PREFIX/glibc/opt/7-Zip/7zFM >/sdcard/Box64Droid.log 2>&1 &")
        os.system("am start -n com.termux.x11/com.termux.x11.MainActivity &>/dev/null")
        stop = input()
        if stop == "2":
            print(" Stopping Wine...")
            os.system("box64 wineserver -k &>/dev/null")
            main_menu()
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
    elif choice == "3":
        change_wine_version()
        main_menu()
    elif choice == "4":
        recreate_prefix()
        main_menu()
    elif choice == "5":
        os.system("wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/native/checkupdates.py &>/dev/null && mv checkupdates.py $PREFIX/bin")
        os.system("python3 $PREFIX/bin/checkupdates.py")
    elif choice == "6":
        os.system("clear")
        os.system(r"unset LD_PRELOAD; export GLIBC_PREFIX=/data/data/com.termux/files/usr/glibc; export PATH=$GLIBC_PREFIX/bin:$PATH; cd ~/; git clone https://github.com/ptitSeb/box64; cd ~/box64; sed -i 's/\/usr/\/data\/data\/com.termux\/files\/usr\/glibc/g' CMakeLists.txt; sed -i 's/\/etc/\/data\/data\/com.termux\/files\/usr\/glibc\/etc/g' CMakeLists.txt; mkdir build; cd build; cmake --install-prefix $PREFIX/glibc .. -DARM_DYNAREC=1 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DBAD_SIGNAL=ON -DSD845=ON; make -j8; make install; rm -rf ~/box64; cd ~/")
        os.system("python3 $PREFIX/bin/box64droid.py --start")
        exit()
    elif choice == "7":
        os.system("clear")
        print("Starting Winetricks... To back to main menu press Ctrl+c exit from Winetricks in Termux-X11")
        os.system("am start -n com.termux.x11/com.termux.x11.MainActivity &>/dev/null")
        os.system("box64 winetricks >/dev/null 2>&1")
        main_menu()
    elif choice == "8":
        print("")
        print("Stopping Termux-X11...")
        print("")
        os.system('pkill -f "app_process / com.termux.x11"')
        os.system('pkill -f pulseaudio')
        exit()
def start():
    if len(sys.argv) < 2:
        print("Empty argument, use --help to see available arguments")
    elif sys.argv[1] == "--start":
        start_box64droid()
        check_config()
        check_prefix()
        main_menu()
    elif sys.argv[1] == "--startwd":
        start_box64droid()
        check_config()
        check_prefix()
        exit()
    elif sys.argv[1] == "--startwinetrickswd":
        start_box64droid()
        check_config()
        check_prefix()
        print("Starting Winetricks...")
        os.system("sleep 2")
        os.system("am start -n com.termux.x11/com.termux.x11.MainActivity &>/dev/null")
        os.system("box64 winetricks >/dev/null 2>&1")
    elif sys.argv[1] == "--changewineverwd":
        change_wine_version()
        exit()
    elif sys.argv[1] == "--recreateprefix":
        start_box64droid()
        check_config()
        recreate_prefix()
        exit()
    elif sys.argv[1] == "--uninstall":
        print("Uninstalling Box64Droid...")
        glibc_path = "/data/data/com.termux/files/usr/glibc"
        wine_prefix_path ="/data/data/com.termux/files/home/.wine"
        shutil.rmtree(glibc_path)
        shutil.rmtree(wine_prefix_path)
        os.system("rm $PREFIX/bin/box64droid")
        os.system("rm $PREFIX/bin/box64droid.py")
        os.system("rm $PREFIX/bin/start-box64.py")
        os.system("rm -r $HOME/.shortcuts")
    elif sys.argv[1] == "--reinstall":
        os.system("curl -o install https://raw.githubusercontent.com/Ilya114/Box64Droid/main/installers/install.sh && chmod +x install && ./install")
    elif sys.argv[1] == "--version":
        print("31.12.24")
    elif sys.argv[1] == "--help":
        print("Box64Droid (native version) - configured tools to launch Box64, Box86, Wine 8.0, DXVK with Adreno GPU drivers in Termux")
        print("Usage: box64droid {argument}")
        print("Available arguments:")
        print("--start - start Box64Droid")
        print("--uninstall - uninstall Box64Droid (all data in prefix will be clear)")
        print("--reinstall - reinstall Box64Droid (all data in prefix will be clear)")
        print("--version - show current version of Box64Droid")
        print("--help - see this menu and exit")
    else:
        print("Invalid argument, use --help to see available arguments")
if __name__ == "__main__":
    start()
