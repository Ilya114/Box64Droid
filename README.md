# Box64Droid
[![telegram](https://img.shields.io/badge/chat-telegram-brightgreen.svg?logo=telegram&style=flat-square)](https://t.me/box64droichat)
[![discord](https://img.shields.io/discord/308323056592486420?logo=discord)](https://discord.gg/thjpZ4P7Bm)

Box64Droid is a project with scripts that automate installing preconfigured rootfs with [Box64](https://github.com/ptitSeb/box64), [Box86](https://github.com/ptitSeb/box86), [Wine](https://github.com/Kron4ek/Wine-Builds), [DXVK](https://github.com/doitsujin/dxvk), [D8VK](https://github.com/AlpyneDreams/d8vk) on Android. Originally was a [fork](https://github.com/Ilya114/Box4Droid) of [Box4Droid](https://github.com/Herick75/Box4Droid) with Box64.

- News about the project are published on the [Telegram](https://t.me/box64droidch) channel.
- The project site is available [here](https://ilya114.github.io).

## Installation instructions
1. Install [Termux](https://github.com/termux/termux-app/releases/download/v0.118.0/termux-app_v0.118.0+github-debug_arm64-v8a.apk), [Termux-x11](https://github.com/Ilya114/Box64Droid/releases/download/stable/app-arm64-v8a-debug.apk) and [Termux:Widget](https://github.com/termux/termux-widget/releases/download/v0.13.0/termux-widget_v0.13.0+github-debug.apk).
2. In Termux, run the Box64Droid install command, select need version (i recommend native) and wait until it's installed: `curl -o install https://raw.githubusercontent.com/Ilya114/Box64Droid/main/installers/install.sh && chmod +x install && ./install`
3. After the installation is completed, run `box64droid --start`. The script will start Termux-X11 and show the start menu.
4. To use Input Bridge, install 0.1.9 apk and then simply run the app on Android and in Wine from the start menu.

## Launch via homescreen using Termux:Widget (native version)
You can launch and update Box64Droid via start menu, just create Termux:Widget widget and you will see these options

## System requirements

- Adreno 610+ (Other GPUs are supported by VirGL, but many games might not work)
- Android 12+ (non-root, VirGL version), Android 10+ (root version), Android 9+ (native version)
- 64-bit Android
- You also need ~4,2GB (for root version), 4,5GB (for non-root version) or ~3,3GB (for VirGL version) worth of free space for the installation to run without problems.

To increase performance and stability, use the root version (root access required) or the native version (less stable but offers the same performance as the root version).

## Configuring

- You can choose to use environment variables; there are three files: `DXVK_D8VK.conf`, `Box64Droid.conf`, and `DXVK_D8VK.conf`. These files are created and found in the /sdcard/Box64Droid/ folder after the first Box64Droid run.
- The `Box64Droid.conf` file includes configurations for rootfs, Box86, Box64, and Wine. You can utilize the Box86 and Box64 environment variables; you can find more information about them [here](https://github.com/ptitSeb/box86/blob/master/docs/USAGE.md#) and [here](https://github.com/ptitSeb/box64/blob/main/docs/USAGE.md). You can add as many variables as needed.
- The `DXVK_D8VK_HUD.conf` file is intended for using environment variables related to [DXVK_HUD](https://github.com/doitsujin/dxvk#hud).
- The `DXVK_D8VK.conf` file is intended for using environment variables related to [dxvk](https://github.com/doitsujin/dxvk/blob/master/dxvk.conf).

## Known issues

- Very fast "install" (which really failed due a Termux update packages process failed). Clear Termux data will resolve this issue.
- Android 12+ may terminate Termux, displaying `[Process completed (signal 9) - press Enter]`. To resolve this, execute the following command in from your PC (you need [plaform-tools](https://developer.android.com/tools/releases/platform-tools) and enabled ADB debugger in phone): `adb shell "/system/bin/device_config put activity_manager max_phantom_processes 2147483647"`.
- Winetricks takes a long time to run when Proton is installed (non-root version).

## Instructions on how to mount SD-card external HDD/SSD (chroot version only)

If you want to mount an SD card or an external drive (HDD/SSD), you need to add the mountpoint manually. Follow these steps:

1. Mount the drive onto the phone storage:
   - For an SD card, navigate to `/storage` and check the folders (using `sudo ls`), for example, `8D3E-2B7K`.
   - For external drives, navigate to `/mnt/media_rw` and check for a folder like `C3G3H6B8A56212H7`.
2. Mount the drive into the chroot envrionment:
   - Type `nano $PREFIX/bin/box64droid` and add the mount command before the `sudo chroot login ...` line: `sudo mount --bind /mnt/media_rw/drivename (or /storage/sdcardname) $ROOTFSPATH/needfolder`.
   - You need to manually create `needfolder` in the `~/ubuntu` folder by using `sudo mkdir foldername`.

## Applications and scripts which were used in Box64Droid
- [Termux-app](https://github.com/termux/termux-app) - GPLv3 license
- [Box64 by ptitseb](https://github.com/ptitSeb/box64) - MIT license
- [Box86 by ptitseb](https://github.com/ptitSeb/box86) - MIT license
- [Wine Stable, Staging and Staging-tkg GPL-2.1 license](https://wiki.winehq.org/Licensing) (builded by [Kron4ek](https://github.com/Kron4ek) by MIT License), [Wine Proton by Valve](https://github.com/ValveSoftware/Proton) (own license), [Wine GE](https://github.com/GloriousEggroll/wine-ge-custom) (using in Lutris)
- [Mesa](https://docs.mesa3d.org/license.html) - MIT, Khronos, SGI Free Software License B and Boost (permissive) licenses
- [Termux-x11](https://github.com/termux/termux-x11) - GPL-3.0 license
- [DXVK](https://github.com/doitsujin/dxvk) - Zlib license
- [Proot-distro](https://github.com/termux/proot-distro) - GPL-3.0 license
- [Forked Mesa to work Turnip on Adreno 730 and 740](https://gitlab.freedesktop.org/Danil/mesa/-/tree/turnip/feature/a7xx-basic-support)
- [D8VK](https://github.com/AlpyneDreams/d8vk) - Zlib license
- [DXVK-Async](https://github.com/Sporif/dxvk-async)
- [DXVK-GPLAsync](https://gitlab.com/Ph42oN/dxvk-gplasync)
- [WineD3D for Windows](https://fdossena.com/?p=wined3d/index.frag) - GPL-2.0+ license
- [Winetricks](https://wiki.winehq.org/Winetricks)
- [vkd3d-proton](https://github.com/HansKristian-Work/vkd3d-proton) - LGPL v2.1 license
- [glibc-prefix](https://github.com/termux-pacman/glibc-packages) - MIT license

## Thanks to:
- [Herick75](https://github.com/Herick75) - for providing patches that made compiling Mesa Turnip possible
- [Inguna87](https://github.com/inguna87) - for start chroot fix for MIUI and Oxygen
- [Alfhashut](https://github.com/alfhashut) - inspired me to try VirGL again and tried to help me with it
