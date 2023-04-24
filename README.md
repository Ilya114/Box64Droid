## What is Box4Droid?
## Note: currently repo WIP, so it can work not stable
Box4Droid is a simple script that automates the installation of a preconfigured Rootfs with [Box86](https://github.com/ptitSeb/box86), [Box64](https://github.com/ptitSeb/box64), [Wine 7.1 (box86) and 7.20 (box64)](https://www.winehq.org/) and [DXVK](https://github.com/doitsujin/dxvk) installed, made by me. [YouTube: Smartphone Desktop](https://youtube.com/@smartphonedesktop4229).

My fork contains new rootfs with box64 and some useful tools. Mesa version rolled back to 22.3.0 because I can`t compile 23.x now.

## Do you need root?

No, Box4Droid uses proot to run Rootfs, so no, root is not required, but we can use chroot also which requiment root

## How to install?  

First you need to install [Termux](https://f-droid.org/en/packages/com.termux) and [Termux-x11](https://github.com/termux/termux-x11/actions/runs/4385798707).  After installing them, just copy the command `curl -o install https://raw.githubusercontent.com/Ilya114/Box4Droid/main/Scripts/install && chmod +x install && ./install` and paste it in the Termux terminal and wait until the installation completes.

## How to start Box86 + Wine?

After the installation is completed, you just need to start Termux-x11 by typing `start-x11` in the terminal, enter the Termux-x11 app, then go back to Termux, and then type `start-box86`, in seconds Wine will start together with the TFM. 

Note: default starting box86, to start box64 press Ctrl+c then type `./startbox64`

You can also use Input Bridge, just run `installer.bat` and Input Bridge will start automatically.

## System requirements 

- Adreno 618+ (Another GPU`s and Adreno 7xx not working now)

- Android 10+??  

- 64-bit Android 

- You also need at 4,7 GB free for the installation to go without problems.

## How to configure?  

You can choose to use environment variables, there are 3 files, `dxvk.conf`, `Box8664.conf` and `DXVK_env.conf`. These files are created and found in the internal storage inside the Box4Droid folder right after the first run of Box86.

The `Box8664.conf` file is for you to use the Box86 and Box64 environment variables, see all of them [here](https://github.com/ptitSeb/box86/blob/master/docs/USAGE.md#) and [here](https://github.com/ptitSeb/box64/blob/main/docs/USAGE.md). You can add as many variables as you like. In this file, there is the `res` variable, in it you put the same resolution that you chose in Termux-x11, otherwise the screen content may be cut off or there may be borders on the screen.

The `DXVK_env.conf` file is for you to use the environment variables referring to [DXVK_HUD](https://github.com/doitsujin/dxvk#hud), in addition to other settings.  

The `dxvk.conf` file is for you to use the environment variables referring to [dxvk](https://github.com/doitsujin/dxvk/blob/master/dxvk.conf)(To use it, it is necessary to uncomment the line that exports your directory, this variable is found in `DXVK_env.conf`).

## Known issues

- For some reason, when you go to install Termux and use the `pkg update -y` command for the first time, it may happen that you get some error and it is not possible to continue the installation, if that happens, just delete the Termux data and try again.

<details>

![Screenshot](Docs/InShot_20230402_231621771.jpg)
</details>

- Another problem that happens is when you start Box86 for the first time, when you run anything, it will run extremely slow, in this case, it is highly recommended to restart Box86 (in most cases, games will run perfectly after that).

<details>
<summary>Before</summary>

![Screenshot](Docs/Screenshot_2023-04-03-12-27-57-973_com.termux.x11.jpg)
</details>

<details>
<summary>After</summary>

![Screenshot](Docs/Screenshot_2023-04-03-12-29-12-605_com.termux.x11.jpg)
</details>

In Wine, processor cores are not available to be selected via `taskmgr`. GTA IV has infinite loading. I'm looking for a way around this.

<details>

![Screenshot](Docs/Screenshot_2023-04-03-12-40-22-746_com.termux.x11.jpg)
</details>

And there are probably other issues, so feel free to open an issue.

- DXVK not working due a Mesa Turnip 22.x, I`m need to compile 23.x

- "Control" tab in Start menu not open. You can just open `control` using "Run"

- When type `exit` you can have stucked logout. To resolve kill session.

## TO-DO list

Install VirGL for Mali GPUs.

Create a launcher.

## Things to note

Some issues/instabilities can happen when using Box86 in proot environment, so it's not recommended to use Box86 in proot as debug/testing environment, there are better options for that.

## Third party applications

[Box86 by ptitseb](https://github.com/ptitSeb/box86) MIT license

[Proot under Termux](https://github.com/termux/proot) GPL-2.0 license

[DXVK](https://github.com/doitsujin/dxvk) Zlib license

[Termux-app](https://github.com/termux/termux-app) GPLv3 license

[Termux-x11](https://github.com/termux/termux-x11)

[Wine](https://wiki.winehq.org/Licensing)
