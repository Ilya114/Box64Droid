# Box64Droid
# WARNING!!! Still in early stage, therefore there may be problems and shortcomings
Box64Droid is a script that automates the installation of a preconfigured rootfs with [Box86](https://github.com/ptitSeb/box86), [Box64](https://github.com/ptitSeb/box64), [Proton 8.0-2](https://github.com/ValveSoftware/Proton), [DXVK](https://github.com/doitsujin/dxvk) installed. Project based on Box4Droid, original author is [Herick75](https://github.com/Herick75)

Project chat [available](https://t.me/box64droidchat) in Telegram, also there is a [site](https://Ilya114.github.io/Box64Droid/)

## Do I need root?

Box64Droid using proot to run rootfs, so no, root is not required, chroot also can use.

## How to install?  

First you need to install [Termux](https://github.com/termux/termux-app/releases/download/v0.118.0/termux-app_v0.118.0+github-debug_arm64-v8a.apk) and [Termux-x11](https://github.com/Ilya114/Box64Droid/releases/download/beta/app-debug.apk). After installing them, just copy and paste in Termux this command then when Box64Droid install: `curl -o install https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/install && chmod +x install && ./install`

## How to start Box64 + Wine?

After the installation is completed, type `box64droid --start`, starting script will start Termux-X11 and show start menu.

You can also use Input Bridge, install 0.1.9 apk then just run app in Android and in Wine from start menu,

## System requirements 

- Adreno 616+ recommend (Another GPU's supporting but less games work)
- Android 12+ (proot version), Android 10+ (chroot version)
- 64-bit Android 
- You also need at ~4,5 GB (or ~3,3 for VirGL version) free for the installation to go without problems.

## How to configure?  

You can choose to use environment variables, there are 3 files, `dxvk.conf`, `Box8664.conf` and `DXVK_env.conf`. These files are created and found in the internal storage inside the Box64Droid folder right after the first run of Box86 or Box64.

The `Box64Droid.conf` file is for you to use the Box86 and Box64 environment variables, see all of them [here](https://github.com/ptitSeb/box86/blob/master/docs/USAGE.md#) and [here](https://github.com/ptitSeb/box64/blob/main/docs/USAGE.md). You can add as many variables as you like.

The `DXVK_HUD.conf` file is for you to use the environment variables referring to [DXVK_HUD](https://github.com/doitsujin/dxvk#hud), in addition to other settings.  

The `DXVK.conf` file is for you to use the environment variables referring to [dxvk](https://github.com/doitsujin/dxvk/blob/master/dxvk.conf)(To use it, it is necessary to uncomment the line that exports your directory, this variable is found in `DXVK_env.conf`).

## Known issues

- Error when updating Termux packages. Clear Termux data will help.
- Android 12+ can kill Termux, you may get `[Process completed (signal 9) - press Enter]`, to fix run this command in adb shell: `adb shell "/system/bin/device_config put activity_manager max_phantom_processes 2147483647"`
- "Control" menu in Wine (in Proton 8.0-2 working fine) shows nothing. You can just open `control` using "Run"
- Box64Droid can exit after start. This is a TFM issue, no have idea why and how to fix. 
- Winetricks runs a long of time when Proton installed (proot)

If you has other issues like black screen or crashing game/app run Box64 in debug mode then open issue and attach /sdcard/Box64Droid.log

## Instructionsl how to mount SD-card external HDD/SSD (chroot version)

If you want mount sdcard or external HDD (SSD), you need to add mountpoint. For sdcard go to /storage and see folder example `8D3E-2B7K`. For external drivers go to /mnt/media_rw and see folder like `C3G3H6B8A56212H7`. Type `nano $PREFIX/bin/start-box-root` and add mount command before `sudo chroot login ...` line: `sudo mount --bind /mnt/media_rw/drivename (or /storage/sdcardname) $ROOTFSPATH/needfolder`. You need to create `needfolder` yourself in ~/ubuntu folder by using `sudo mkdir foldername` 

## Things to note

Some issues/instabilities can happen when using Box86 and Box64 in proot environment, so it's not recommended to use Box86 and Box64 in proot as debug/testing environment, there are better options for that.

## Third party applications
- [Termux-app](https://github.com/termux/termux-app) GPLv3 license
- [Box64 by ptitseb](https://github.com/ptitSeb/box64) MIT license
- [Box86 by ptitseb](https://github.com/ptitSeb/box86) MIT license
- [Proot-distro](https://github.com/termux/proot-distro) GPL-3.0 license
- [Wine Stable, Staging and Staging-tkg GPL-2.1 license](https://wiki.winehq.org/Licensing) (builded by [Kron4ek](https://github.com/Kron4ek) by MIT License), [Wine Proton by Valve](https://github.com/ValveSoftware/Proton) (own license), [Wine GE](https://github.com/GloriousEggroll/wine-ge-custom) (using in Lutris)
- [Termux-x11](https://github.com/termux/termux-x11) GPL-3.0 license
- [DXVK](https://github.com/doitsujin/dxvk) Zlib license
- [WineD3D for Windows](https://fdossena.com/?p=wined3d/index.frag) GPL-2.0+ License
- [Winetricks](https://wiki.winehq.org/Winetricks)

## Thanks to:
- [Herick75](https://github.com/Herick75) - for Mesa Turnip patches which make possible compile it
- [Inguna87](https://github.com/inguna87) - for start chroot fix for MIUI and probably Oxygen
- [Alfhashut](https://github.com/alfhashut) - inspired me to try VirGL again and trying help me with him
