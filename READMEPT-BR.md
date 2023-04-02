# O que é Box4Droid?

Box4Droid é um script que automatiza a instalação de um Rootfs pré-configurado com Box86 e Wine 7.1 instalado feito por mim[].

# Como instalar?

É simples, basta copiar `curl -o install https://raw.githubusercontent.com/Herick75/Box4Droid/main/Scripts/install && chmod +x install && ./install`
e passe-o no terminal Termux e aguarde até que a instalação seja concluída.

# Compatibilidade

Por enquanto, apenas GPUs Adreno compatíveis com
Motorista Turnip Funcionará com aceleração 3D.

Esta Wine 7.1 já vem com o DXVK 2.1 instalado.  Você também pode alterar as versões através do menu Iniciar da Wine.

OpenGL também funciona, mas você não pode usar OpenGL>DirectX
Camada por enquanto (somente se você quiser instalar manualmente
dlls wined3d).

# Como configurar?

Você pode optar por usar variáveis de ambiente,existem 3 arquivos,o `dxvk.conf`, o `Box86.conf` e o `DXVK_env.conf`.Estes arquivos são criados e se encontram na armazenamento
interno dentro da pasta Box4Droid logo após a primeira execução do Box86. 

O arquivo `Box86.conf` serve para você usar as variáveis de ambiente do Box86, você pode adicionar quantas variáveis quiser.

O arquivo `DXVK_env.conf serve para você usar as variáveis de ambiente referentes ao DXVK_HUD, além de outras configurações.

O arquivo `dxvk.conf` serve para você usar as variáveis de ambiente referentes ao dxvk.
