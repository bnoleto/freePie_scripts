# freePie_scripts
Python scripts to customize gamepads on Windows. [vJoy](http://vjoystick.sourceforge.net/site/index.php/download-a-install/download) and [freePie](https://github.com/AndersMalmgren/FreePIE/releases) are required for any of them to work. To use the scripts for DualShock3 controllers, I recommend installing [nefarius' ScpToolkit](https://github.com/nefarius/ScpToolkit/releases).

## Script notes
* [race_ds3_controller.py](https://github.com/bnoleto/freePie_scripts/blob/master/race_ds3_controller.py): Basic script with center reduction. Can be used in general racing games.
* [race_mouse.py](https://github.com/bnoleto/freePie_scripts/blob/master/race_mouse.py): Allows you to use the mouse to precisely control the steering in racing games, plus some key assignments for smooth acceleration. Works incredibly nice in games such as Codemasters' F1 Series and simulators such as Project Cars. Although it is really painful assigning the axis within these games, the results are almost perfect.
  * *Hint: Change the STEERING_SENSITIVITY to a value you prefer. With the mouse at 3200dpi, 0.2 sensitivity is great in F1 2018, while 0.1 sensitivity is very good in Project Cars. Use the LEFT MOUSE BUTTON to accelerate, and the RIGHT MOUSE BUTTON to brake. If you do any of these commands while holding the LSHIFT key, the axis increment/decrement rate will be faster, and if you do that holding the LCTRL key, the the axis increment/decrement rate will be slower. The steering sensitivity never changes.*

![Mouse Steering](https://i.imgur.com/sjQaiQu.png)
  
* [race_xone_controller.py](https://github.com/bnoleto/freePie_scripts/blob/master/race_xone_controller.py): Almost the same as race_ds3_controller, but I tried some tweaking to take advantage of the precision of the Xbox One controller. I don't know exactly why I did this.
* [flightsim_xone_controller.py](https://github.com/bnoleto/freePie_scripts/blob/master/flightsim_xone_controller.py): Script with center reduction on all axis. The left Analog Y axis is used for throttle purposes in flight simulators. Press X with idle thrust, and pull down the right analog to use reverse thrust. Pull up the same analog and press X again to go back to normal thrust. Press A to change to ground mode. The left/right triggers will now be the left/right brakes of the aircraft. And the yaw/front gear control will now be controlled from the left analog. Rolling maneuvers are disabled in this mode.Press A again to switch back to normal controls.
## Useful links
* scpToolkit - https://github.com/nefarius/ScpToolkit
* freePIE - https://github.com/AndersMalmgren/FreePIE
* vJoy - http://vjoystick.sourceforge.net

## (Português)
Scripts em Python para customizar controles no Windows. [vJoy](http://vjoystick.sourceforge.net/site/index.php/download-a-install/download) e [freePie](https://github.com/AndersMalmgren/FreePIE/releases) são obrigatórios para que qualquer dos scripts funcionem. Para usar os scripts com um controle DualShock3, eu recomendo instalar o [ScpToolkit modificado pelo Nefarius.](https://github.com/nefarius/ScpToolkit/releases)

## Notas
As atribuições dos botões ainda não estão implementadas. Estou usando as atribuições padrão do controle virtual do Xbox360 para isso.

* [race_ds3_controller.py](https://github.com/bnoleto/freePie_scripts/blob/master/race_ds3_controller.py): Script básico com redução de centro. Pode ser utilizado em jogos de corrida.
* [race_mouse.py](https://github.com/bnoleto/freePie_scripts/blob/master/race_mouse.py): Permite que você utilize o mouse para controlar precisamente a direção em jogos de corrida, fora algumas atribuições de tecla para uma aceleração suave. Funciona incrivelmente bem em jogos tipo a série F1 da Codemasters e simuladores como Project Cars. Embora seja um parto pra configurar os eixos nesses jogos, os resultados são quase perfeitos.
  * *Dica: Altere o valor da STEERING_SENSITIVITY para o que você preferir. Usando o mouse a 3200dpi, a sensibilidade de 0.2 é ótima para o F1 2018, enquanto a sensibilidade de 0.1 é muito boa para o Project Cars. Use o BOTÃO ESQUERDO DO MOUSE para acelerar, e o BOTÃO DIREITO DO MOUSE para frear. Caso você dê algum desses comandos enquanto pressiona SHIFT ESQUERDO, a taxa de incremento/decremento do eixo será maior, e se você fizer o mesmo enquanto pressiona CTRL ESQUERDO, a taxa de incremento/decremento do eixo será menor. A sensibilidade da direção nunca se altera.*
* [race_xone_controller.py](https://github.com/bnoleto/freePie_scripts/blob/master/race_xone_controller.py): Quase a mesma coisa do race_ds3_controller, mas tentei fazer algumas alterações pra tentar tirar proveito da precisão do controle do XboxOne. Não sei muito bem por que eu fiz isso.
* [flightsim_xone_controller.py](https://github.com/bnoleto/freePie_scripts/blob/master/flightsim_xone_controller.py): Script com redução de centro em todos os eixos. O eixo Y do analog direito é usado para aceleração em simuladores de vôo. Pressione X com o manete no mínimo, e puxe o analog direito pra baixo para utilizar o reverso. Para voltar ao normal, puxe o analog para cima totalmente até a propulsão voltar ao mínimo e pressione X novamente. Pressione A para mudar para os controles de solo. Os triggers esquerdo e direito, agora serão os respectivos freios da aeronave. E o leme/controle do trem de pouso dianteiro passará a ser controlado pelo analog esquerdo. Manobras de giro no avião são desabilitadas nesse modo. Pressione A novamente para voltar os controles ao normal.
