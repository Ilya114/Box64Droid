# O que é Box4Droid?

Box4Droid é um script simples que automatiza a instalação de um Rootfs pré-configurado com o Box86, com a Wine 7.1 e com a DXVK instalado,feito por mim.[YouTube: Smartphone Desktop](https://youtube.com/@smartphonedesktop4229).

# É preciso ter root?

Não, Box4Droid usa o proot para executar o Rootfs, então não, não é nescessário root.

# Como instalar?

Primeiramente você precisa instalar o [Termux](https://f-droid.org/en/packages/com.termux) e o [Termux-x11](https://github.com/termux/termux-x11/actions/runs/4385798707).

Após instalar eles, basta copiar o comando `curl -o install https://raw.githubusercontent.com/Herick75/Box4Droid/main/Scripts/install && chmod +x install && ./install`
e cole no terminal do Termux e aguarde até que a instalação seja concluída.

# Como iniciar o Box86 + Wine?

Depois da instalação ser concluída, você só precisa iniciar o Termux-x11 digitando `x11` no terminal,entrar no app Termux-x11,e em seguida digitar `start-box86`,em segundos a Wine já vai iniciar junto com o TFM.

Você também pode usar o Input Bridge, basta inciar o aplicativo e tudo já estará funcionando (caso a engrenagem não apareça,basta executar o `installer.bat`)

# Compatibilidade

Por enquanto, apenas GPUs Adreno compatíveis com
o driver Turnip vão funcionar com aceleração 3D.

Esta Wine 7.1 já vem com o DXVK 2.1 instalado.  Você também pode alterar as versões através do menu Iniciar da Wine.

OpenGL também funciona, mas você não pode usar a camada wined3d(OpenGL>DirectX)
por enquanto (somente se você quiser instalar manualmente as
dlls wined3d).

# Como configurar?

Você pode optar por usar variáveis de ambiente,existem 3 arquivos,o `dxvk.conf`, o `Box86.conf` e o `DXVK_env.conf`.Estes arquivos são criados e se encontram no armazenamento
interno dentro da pasta Box4Droid logo após a primeira execução do Box86. 

O arquivo `Box86.conf` serve para você usar as variáveis de ambiente do Box86, você pode adicionar quantas variáveis quiser.

O arquivo `DXVK_env.conf` serve para você usar as variáveis de ambiente referentes ao DXVK_HUD, além de outras configurações.

O arquivo `dxvk.conf` serve para você usar as variáveis de ambiente referentes ao dxvk(Para usá-lo, é nescessário descomentar a linha que exporta o seu diretorio, está variavel se encontra em `Box86.conf`).

# Problemas conhecidos

Por algum motivo, quando você vai instalar o Termux e usar o comando `pkg update -y` pela primeira vez,pode acontecer de dar algum erro e não ser possível de continuar a instalação, se isso acontecer, apenas apague os dados do Termux e tente novamente.
![Screenshot](Docs/InShot_20230402_231621771.jpg)

# TO-DO list

Instalar a VirGL para GPUs Mali.

Criar um launcher.

# Coisas a serem observadas 

Alguns problemas/instabilidades podem acontecer ao usar o Box86 em ambiente proot, então não é recomendado usar o Box86 no proot como ambiente de debug,existem opções melhores para isso.

# Aplicativos de terceiros
[Box86](https://github.com/ptitSeb/box86) MIT license

[Anlinux Ubuntu Rootfs](https://github.com/EXALAB/Anlinux-Resources/tree/master/Rootfs/Ubuntu/arm64) GPL-2.0 License

[Termux-app](https://github.com/termux/termux-app) GPLv3 license

[Termux-x11](https://github.com/termux/termux-x11)  GPL-3.0 license

