# O que é Box4Droid?

Box4Droid é um script simples que automatiza a instalação de um Rootfs pré-configurado com o [Box86](https://github.com/ptitSeb/box86), com a [Wine 7.1](https://www.winehq.org/) e com a [DXVK](https://github.com/doitsujin/dxvk) instalado,feito por mim.[YouTube: Smartphone Desktop](https://youtube.com/@smartphonedesktop4229).

# É preciso ter root?

Não, Box4Droid usa o proot para executar o Rootfs, então não, não é nescessário root.

# Como instalar?

Primeiramente você precisa instalar o [Termux](https://f-droid.org/en/packages/com.termux) e o [Termux-x11](https://github.com/termux/termux-x11/actions/runs/4385798707).

Após instalar eles, basta copiar o comando `curl -o install https://raw.githubusercontent.com/Herick75/Box4Droid/main/Scripts/install && chmod +x install && ./install`
e cole no terminal do Termux e aguarde até que a instalação seja concluída.

# Como iniciar o Box86 + Wine?

Depois da instalação ser concluída, você só precisa iniciar o Termux-x11 digitando `x11` no terminal,entrar no app Termux-x11,e em seguida voltar no app do Termux e digitar `start-box86`,em segundos a Wine já vai iniciar junto com o TFM.

Você também pode usar o Input Bridge, basta executar o `installer.bat` e o Input Bridge já irá iniciar automaticamente.

# Requisitos do sistema

*Adreno 618+

*Android 10+??

*64-bit Android

Você também precisa de no mínimo 4GB livres para a instalação ocorrer sem problemas.

# Como configurar?

Você pode optar por usar variáveis de ambiente,existem 3 arquivos,o `dxvk.conf`, o `Box86.conf` e o `DXVK_env.conf`.Estes arquivos são criados e se encontram no armazenamento
interno dentro da pasta Box4Droid logo após a primeira execução do Box86. 

O arquivo `Box86.conf` serve para você usar as variáveis de ambiente do Box86,veja todas elas [aqui](https://github.com/ptitSeb/box86/blob/master/docs/USAGE.md#usage). Você pode adicionar quantas variáveis quiser.Neste arquivo, tem a variável `res`, nela você coloca a mesma resolução que você escolheu no Termux-x11, caso contrário, o conteúdo da tela pode ser cortado ou pode haver bordas na tela.

O arquivo `DXVK_env.conf` serve para você usar as variáveis de ambiente referentes ao [DXVK_HUD](https://github.com/doitsujin/dxvk#hud), além de outras configurações.

O arquivo `dxvk.conf` serve para você usar as variáveis de ambiente referentes ao [dxvk](https://github.com/doitsujin/dxvk/blob/master/dxvk.conf)(Para usá-lo, é nescessário descomentar a linha que exporta o seu diretorio, está variavel se encontra em `Box86.conf`).

# Problemas conhecidos

Por algum motivo, quando você vai instalar o Termux e usar o comando `pkg update -y` pela primeira vez,pode acontecer de dar algum erro e não ser possível de continuar a instalação, se isso acontecer, apenas apague os dados do Termux e tente novamente.
![Screenshot](Docs/InShot_20230402_231621771.jpg)

Outro problema que acontece é quando você vai iniciar o Box86 pela primeira vez, quando você for executar qualquer coisa, vai rodar extremamente lento,neste caso, é super recomendado reiniciar o Box86 (na maioria dos casos, os jogos já iram rodar perfeitamente após isso).

Antes
![Screenshot](Docs/Screenshot_2023-04-03-12-27-57-973_com.termux.x11.jpg)

Depois
![Screenshot](Docs/Screenshot_2023-04-03-12-29-12-605_com.termux.x11.jpg)

Na Wine,os núcleo do processador não estão disponíveis para serem selecionados através do `taskmgr`. GTA IV fica com o carregamento infinito. Estou procurando alguma forma de contornar isso.

![Screenshot](Docs/Screenshot_2023-04-03-12-40-22-746_com.termux.x11.jpg)

E provavelmente deve ter outros problemas, então sinta-se livre para emitir algum problema.

# TO-DO list

Instalar a VirGL para GPUs Mali.

Criar um launcher.

# Coisas a serem observadas 

Alguns problemas/instabilidades podem acontecer ao usar o Box86 em ambiente proot, então não é recomendado usar o Box86 no proot como ambiente de debug/testes, existem opções melhores para isso.

# Aplicativos de terceiros
[Box86 by ptitseb](https://github.com/ptitSeb/box86) MIT license

[Proot under Termux](https://github.com/termux/proot) GPL-2.0 license

[Anlinux Ubuntu Rootfs](https://github.com/EXALAB/Anlinux-Resources/tree/master/Rootfs/Ubuntu/arm64) GPL-2.0 License

[DXVK](https://github.com/doitsujin/dxvk) Zlib license

[Termux-app](https://github.com/termux/termux-app) GPLv3 license

[Termux-x11](https://github.com/termux/termux-x11)  GPL-3.0 license

[Wine](https://wiki.winehq.org/Licensing)
