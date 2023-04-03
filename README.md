## Para a versão em PT-BR,[clique aqui.](https://github.com/Herick75/Box4Droid/blob/main/READMEPT-BR.md)

# What is Box4Droid?

Box4Droid is a simple script that automates the installation of a preconfigured Rootfs with Box86, Wine 7.1 and DXVK installed, made by me.[YouTube: Smartphone Desktop](https://youtube.com/@smartphonedesktop4229).

# Do you need root?

No, Box4Droid uses proot to run Rootfs, so no, root is not required.

# How to install?  

First you need to install [Termux](https://f-droid.org/en/packages/com.termux) and [Termux-x11](https://github.com/termux/termux-x11/actions/runs/4385798707).  After installing them, just copy the command `curl -o install https://raw.githubusercontent.com/Herick75/Box4Droid/main/Scripts/install && chmod +x install && ./install` and paste it in the Termux terminal and wait until the installation completes.

# How to start Box86 + Wine?

After the installation is completed, you just need to start Termux-x11 by typing `x11` in the terminal, enter the Termux-x11 app, then go back to Termux, and then type `start-box86`, in seconds Wine will start together with the TFM.

# Compatibility 

For now, only Adreno GPUs compatible with the Turnip driver will work with 3D acceleration.  

This Wine 7.1 already comes with DXVK 2.1 installed.  You can also change versions through Wine's Start menu.  

OpenGL also works, but you can't use the wined3d(OpenGL>DirectX) layer for now (only if you want to manually install the wined3d dlls).  

# How to configure?  

You can choose to use environment variables, there are 3 files, `dxvk.conf`, `Box86.conf` and `DXVK_env.conf`. the first run of Box86.  

The `Box86.conf` file is for you to use the Box86 environment variables, see all of them [here](https://github.com/ptitSeb/box86/blob/master/docs/USAGE.md#box86_dynarec_fastround-) .  You can add as many variables as you like.  

The `DXVK_env.conf` file is for you to use the environment variables referring to [DXVK_HUD](https://github.com/doitsujin/dxvk#hud), in addition to other settings.  

The `dxvk.conf` file is for you to use the environment variables referring to [dxvk](https://github.com/doitsujin/dxvk/blob/master/dxvk.conf)(To use it, it is necessary to uncomment the line that exports your directory, this variable is found in `DXVK_env.conf`).

# known issues

For some reason, when you go to install Termux and use the `pkg update -y` command for the first time, it may happen that you get some error and it is not possible to continue the installation, if that happens, just delete the Termux data and try again.

![Screenshot](Docs/InShot_20230402_231621771.jpg)

# TO-DO list

Install VirGL for Mali GPUs.

Create a launcher.

Box86 and Box64 included.

# Third party applications

[Box86 by ptitseb](https://github.com/ptitSeb/box86) MIT license

[Proot under Termux](https://github.com/termux/proot) GPL-2.0 license

[Anlinux Ubuntu Rootfs](https://github.com/EXALAB/Anlinux-Resources/tree/master/Rootfs/Ubuntu/arm64) GPL-2.0 License

[DXVK](https://github.com/doitsujin/dxvk) Zlib license

[Termux-app](https://github.com/termux/termux-app) GPLv3 license

[Termux-x11](https://github.com/termux/termux-x

[Wine](https://wiki.winehq.org/Licensing
