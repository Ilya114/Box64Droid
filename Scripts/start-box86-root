#!/bin/sh
clear
echo -e ""
export PATH=/sbin:/usr/bin:/usr/sbin:/system/bin:/system/xbin:$PATH
export USER=root
export HOME=/root
dir=/data/data/com.termux/files/home/Ubuntu-fs

echo -e "Montando pastas do sistema ..."

echo -e "/dev"

busybox mount --bind /dev $folder/dev

echo " /sys"

busybox mount --bind /sys $folder/sys

echo " /proc"

busybox mount --bind /proc $folder/proc

echo " /dev/pts"

busybox mount --bind /dev/pts $folder/dev/pts

echo " Memória interna"

busybox mount --bind /storage/ $folder/sdcard

echo -e " Concluído."

echo -e " Iniciando ..."

busybox chroot $folder /bin/su - root

echo -e " Desmontando partições do sistema ..."

echo -e " Desmontando /dev/pra

busybox umount $folder/dev/pts

echo -e " Desmontando /dev"

busybox umount $folder/dev

echo -e " Desmontando /proc"

busybox umount $folder/proc

echo -e " Desmontando memória interna"

busybox umount $folder/sdcard

echo -e " Desmontando /sys"

busybox umount $folder/sys

echo -e " \x1b[32mSistema desmontado com sucesso.\e[0m"
