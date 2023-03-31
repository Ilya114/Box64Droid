echo -e " \x1b[33m [[Iniciando instalação automática, aguarde...]]" & sleep 1
pkg install x11-repo -y
echo -e " \x1b[33m [[Repositório x11-repo instalado]]" & sleep 0.5
echo -e " \x1b[33m [[Baixando e instalando Script de inicialização do servidor x11]]"
wget https://raw.githubusercontent.com/Herick75/Box4Droid/main/Scripts/x11
chmod +x x11
mv x11 $PREFIX/bin
echo -e " \x1b[33m [[Script instalado]]"
echo -e " \x1b[33m [[Instalando pacotes adicionais]]"
pkg install xorg-server-xvfb pulseaudio xwayland -y
echo -e " \x1b[33m [[Baixando e instalando o pacote do Termux-x11]]"
wget https://github.com/Herick75/Box4Droid/raw/main/Apps/termux-x11-1.02.07-0-all.deb
dpkg -i termux-x11-1.02.07-0-all.deb
echo -e " \x1b[33m [[Instalação concluida, para iniciar o servidor x11,basta digitar "x11" no terminal!!]]"

echo -e " \x1b[33m [[Quando for para de usar o servidor x11, é recomendado forçar a parada do Termux pelas configurações Você tambem pode usar o comando 'kill' + o pid do Termux-X11(para saber o pid,basta escrever termux-x11,e no final vai aparecer o id)]]"

