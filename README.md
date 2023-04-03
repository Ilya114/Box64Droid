## Para a versão em PT-BR,[clique aqui.](https://github.com/Herick75/Box4Droid/blob/main/READMEPT-BR.md)

# What is Box4Droid?  

Box4Droid is a simple script that automates the installation of a preconfigured Rootfs with Box86, Wine 7.1 and DXVK installed, made by me.[YouTube: Smartphone Desktop](https://youtube.com/@smartphonedesktop4229 ).  

# Do you need root?

No, Box4Droid uses proot to run Rootfs, so no, root is not required.

# How to install?  

First you need to install [Termux](https://f-droid.org/en/packages/com.termux) and [Termux-x11](https://github.com/termux/termux-x11/actions/runs/4385798707).  After installing them, just copy the command `curl -o install https://raw.githubusercontent.com/Herick75/Box4Droid/main/Scripts/install && chmod +x install && ./install` and paste it in the Termux terminal and wait until the installation completes.  

# Compatibility 

For now, only Adreno GPUs compatible with the Turnip driver will work with 3D acceleration.  

This Wine 7.1 already comes with DXVK 2.1 installed.  You can also change versions through Wine's Start menu.  

OpenGL also works, but you can't use the wined3d(OpenGL>DirectX) layer for now (only if you want to manually install the wined3d dlls).  

# How to configure?  

You can choose to use environment variables, there are 3 files, `dxvk.conf`, `Box86.conf` and `DXVK_env.conf`. 

These files are created and found in the internal storage inside the Box4Droid folder right after the first run of Box86

The `Box86.conf` file is for you to use the Box86 environment variables, you can add as many variables as you want.  

The `DXVK_env.conf` file is for you to use the environment variables referring to the DXVK_HUD, in addition to other settings.  

The `dxvk.conf` file is for you to use the environment variables related to dxvk (To use it, it is necessary to uncomment the line that exports your directory, this variable is found in `Box86.conf`).  

# Third Party Applications 

[Anlinux Ubuntu Rootfs](https://github.com/EXALAB/Anlinux-Resources/tree/master/Rootfs/Ubuntu/arm64) GPL-2.0 License 

[Termux-app](https://github.com/termux/termux-app) GPLv3 license 

[Termux-x11](https://github.com/termux/termux-x11) GPL-3.0 license

