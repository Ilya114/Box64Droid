## What is Box64Droid?
Box64Droid is a simple script that automates the installation of a preconfigured Rootfs with [Box86](https://github.com/ptitSeb/box86), [Box64](https://github.com/ptitSeb/box64), [Wine 7.20](https://www.winehq.org/) and [DXVK](https://github.com/doitsujin/dxvk) installed, made by me. Project based on Box4Droid, original author is [Herick75](https://github.com/Herick75)

## Do you need root?

No, Box64Droid uses proot to run rootfs, so no, root is not required. If you have root, you can use chroot, run `start-box-root` 
If you have /dev /proc /sys /sdcard error no such file or directory create it:
```
mkdir /data/data/com.termux/files/usr/var/lib/proot-distro/installed-rootfs/ubuntu/dev

mkdir /data/data/com.termux/files/usr/var/lib/proot-distro/installed-rootfs/ubuntu/sys

mkdir /data/data/com.termux/files/usr/var/lib/proot-distro/installed-rootfs/ubuntu/proc

mkdir /data/data/com.termux/files/usr/var/lib/proot-distro/installed-rootfs/ubuntu/dev/pts

mkdir /data/data/com.termux/files/usr/var/lib/proot-distro/installed-rootfs/ubuntu/sdcard
```

## How to install?  

First you need to install [Termux](https://f-droid.org/en/packages/com.termux) and [Termux-x11](https://github.com/termux/termux-x11/actions/runs/4385798707).  After installing them, just copy the command `curl -o install https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/install && chmod +x install && ./install` and paste it in the Termux terminal and wait until the installation completes.

## How to start Box + Wine?

After the installation is completed, you just need to start Termux-x11 by typing `start-x11` in the terminal, enter the Termux-x11 app, then go back to Termux, and then type `start-box86`, starting script will ask what's need start: Box86 or Box64

You can also use Input Bridge, just run it from Start menu.

## System requirements 

- Adreno 616+ (Another GPU`s and Adreno 7xx not working now)

- Android 10+??  

- 64-bit Android 

- You also need at 4,7 GB free for the installation to go without problems.

## How to configure?  

You can choose to use environment variables, there are 3 files, `dxvk.conf`, `Box8664.conf` and `DXVK_env.conf`. These files are created and found in the internal storage inside the Box64Droid folder right after the first run of Box86 or Box64.

The `Box8664.conf` file is for you to use the Box86 and Box64 environment variables, see all of them [here](https://github.com/ptitSeb/box86/blob/master/docs/USAGE.md#) and [here](https://github.com/ptitSeb/box64/blob/main/docs/USAGE.md). You can add as many variables as you like. In this file, there is the `res` variable, in it you put the same resolution that you chose in Termux-x11, otherwise the screen content may be cut off or there may be borders on the screen.

The `DXVK_env.conf` file is for you to use the environment variables referring to [DXVK_HUD](https://github.com/doitsujin/dxvk#hud), in addition to other settings.  

The `dxvk.conf` file is for you to use the environment variables referring to [dxvk](https://github.com/doitsujin/dxvk/blob/master/dxvk.conf)(To use it, it is necessary to uncomment the line that exports your directory, this variable is found in `DXVK_env.conf`).

## Known issues

- "Control" tab in Start menu not open. You can just open `control` using "Run"

And there are probably other issues, so feel free to open an issue.

## TO-DO list

Install VirGL for Mali GPUs.

Create a launcher.

## Things to note

Some issues/instabilities can happen when using Box86 and Box64 in proot environment, so it's not recommended to use Box86 and Box64 in proot as debug/testing environment, there are better options for that.

## Third party applications

- [Box86 by ptitseb](https://github.com/ptitSeb/box86) MIT license

- [Box64 by ptitseb](https://github.com/ptitSeb/box64) MIT license

- [Proot-distro](https://github.com/termux/proot-distro) GPL-3.0 license

- [DXVK](https://github.com/doitsujin/dxvk) Zlib license

- [Termux-app](https://github.com/termux/termux-app) GPLv3 license

- [Termux-x11](https://github.com/termux/termux-x11)

- [Wine](https://wiki.winehq.org/Licensing)

- [Winetricks](https://wiki.winehq.org/Winetricks)
