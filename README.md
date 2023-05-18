# Box64Droid
Box64Droid is a script that automates the installation of a preconfigured rootfs with [Box86](https://github.com/ptitSeb/box86), [Box64](https://github.com/ptitSeb/box64), [Proton 8.0-2](https://github.com/ValveSoftware/Proton), [DXVK](https://github.com/doitsujin/dxvk) and [vkd3d-proton](https://github.com/HansKristian-Work/vkd3d-proton) installed. Project based on Box4Droid, original author is [Herick75](https://github.com/Herick75)

Project chat [available](https://t.me/box64droidchat) in Telegram

## Do I need root?

Box64Droid using proot to run rootfs, so no, root is not required, chroot also can use.

## How to install?  

First you need to install [Termux](https://f-droid.org/en/packages/com.termux) and [Termux-x11](https://raw.githubusercontent.com/Ilya114/Box64Droid/main/apps/app-debug.apk). After installing them, just copy and paste in Termux this command then when Box64Droid install: `curl -o install https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/install && chmod +x install && ./install`

If you have Mali, PowerVR or Adreno below 616 you can use rootfs with VirGL (Not stable and much games maybe not working): `curl -o install-virgl https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/install-virgl && chmod +x install-virgl && ./install-virgl`

If you have root, you can use chroot version instead of proot: `curl -o install-root https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/install-root && chmod +x install-root && ./install-root`

## How to start Box + Wine?

After the installation is completed, type `start-box`, starting script will start Termux-X11 and show start menu.

You can also use Input Bridge, install 0.1.9 apk then just run app in Android and in Wine from start menu,

### System requirements 

- Adreno 616+ (Another GPU's and Adreno 7xx not working now)
- Android 11+ 
- 64-bit Android 
- You also need at 5,3 GB free for the installation to go without problems.

## How to configure?  

You can choose to use environment variables, there are 3 files, `dxvk.conf`, `Box8664.conf` and `DXVK_env.conf`. These files are created and found in the internal storage inside the Box64Droid folder right after the first run of Box86 or Box64.

The `Box8664.conf` file is for you to use the Box86 and Box64 environment variables, see all of them [here](https://github.com/ptitSeb/box86/blob/master/docs/USAGE.md#) and [here](https://github.com/ptitSeb/box64/blob/main/docs/USAGE.md). You can add as many variables as you like.

The `DXVK_env.conf` file is for you to use the environment variables referring to [DXVK_HUD](https://github.com/doitsujin/dxvk#hud), in addition to other settings.  

The `dxvk.conf` file is for you to use the environment variables referring to [dxvk](https://github.com/doitsujin/dxvk/blob/master/dxvk.conf)(To use it, it is necessary to uncomment the line that exports your directory, this variable is found in `DXVK_env.conf`).

## Known issues

- "Control" tab in Start menu not open. You can just open `control` using "Run"
- Proton not working in Box86 (seems Box86 problem, asked ptitSeb)
- Can't install Proton versions lower than 8 (will be use only 8.0-2)

And there are probably other issues, so feel free to open an issue.

## Things to note

Some issues/instabilities can happen when using Box86 and Box64 in proot environment, so it's not recommended to use Box86 and Box64 in proot as debug/testing environment, there are better options for that.

## Third party applications
- [Termux-app](https://github.com/termux/termux-app) GPLv3 license
- [Box64 by ptitseb](https://github.com/ptitSeb/box64) MIT license
- [Box86 by ptitseb](https://github.com/ptitSeb/box86) MIT license
- [Proot-distro](https://github.com/termux/proot-distro) GPL-3.0 license
- [Wine](https://wiki.winehq.org/Licensing) GPL-2.1 license
- [Termux-x11](https://github.com/termux/termux-x11) GPL-3.0 license
- [DXVK](https://github.com/doitsujin/dxvk) Zlib license 
- [Winetricks](https://wiki.winehq.org/Winetricks)
- [Vkd3d-proton](https://github.com/HansKristian-Work/vkd3d-proton) GPL-2.1 license

## Thanks to:
- [Herick75](https://github.com/Herick75) - for Mesa Turnip patches which make possible compile it
- [Inguna87](https://github.com/inguna87) - for start chroot fix for MIUI and probably Oxygen
- [Alfhashut](https://github.com/alfhashut) - inspired me to try VirGL again and trying help me with him
