# What is Box4Droid?

Box4Droid is a script that automates the installation of a preconfigured Rootfs with Box86 and Wine 7.1 installed.

# How to install?

It's simple,just copy curl -o install https://raw.githubusercontent.com/Herick75/Box4Droid/main/Scripts/install && chmod +x install && ./install
and past it on Termux terminal and wait until the installation finish.

# Compatibility

For now,only Adreno GPU's that is compatible with
Turnip driver Will work with 3D acceleration.

This Wine 7.1 already comes with DXVK 2.1 installed. You can also change versions through Wine's Start menu.

OpenGL also Works,but you cant use OpenGL>DirectX
Layer for now(only if you want manually installs
wined3d dlls.
