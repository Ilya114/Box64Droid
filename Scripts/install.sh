echo -e " \x1b[33m [[Iniciando instalação automática, aguarde...]]" & sleep 1 &>/dev/null
pkg install x11-repo -y &>/dev/null
echo -e "[[Repositório x11-repo instalado]]" & sleep 0.5 & sleep 1 &>/dev/null
echo -e "[[Baixando e instalando Script de inicialização do servidor x11]]"
wget https://raw.githubusercontent.com/Herick75/Box4Droid/main/Scripts/x11 &>/dev/null
chmod +x x11
mv x11 $PREFIX/bin
echo -e "[[Script instalado]]"
echo -e "[[Instalando pacotes adicionais]]"
pkg install xorg-server-xvfb pulseaudio xwayland -y &>/dev/null
echo -e "[[Baixando e instalando o pacote do Termux-x11]]"
wget https://github.com/Herick75/Box4Droid/raw/main/Apps/termux-x11-1.02.07-0-all.deb &>/dev/null
dpkg -i termux-x11-1.02.07-0-all.deb &>/dev/null
rm -rf install.sh &>/dev/null
echo -e " \x1b[32m\033[[Instalação concluida, para iniciar o servidor x11,basta digitar "x11" no terminal!!]]"
echo -e ""
echo -e ""
echo -e " \x1b[32m\033 [[Quando for para de usar o servidor x11, é recomendado forçar a parada do Termux pelas configurações Você tambem pode usar o comando 'kill' + o pid do Termux-X11(para saber o pid,basta escrever termux-x11,e no final vai aparecer o id)]]"

