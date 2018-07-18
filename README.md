# freePie_scripts
Python scripts to customize gamepads on Windows. [vJoy](http://vjoystick.sourceforge.net/site/index.php/download-a-install/download) and [freePie](https://github.com/AndersMalmgren/FreePIE/releases) are required for any of them to work. To use the scripts for DualShock3/XboxOne controllers, you will need to install [nefarius' ScpToolkit](https://github.com/nefarius/ScpToolkit/releases).

## Script notes
Buttons assignments aren't implemented yet. I'm using the scpToolkit's virtual Xbox360 Controller assignments for that.
* [race_ds3.py](https://github.com/bnoleto/freePie_scripts/blob/master/race_ds3.py): Basic script with center reduction. Can be used in general racing games.
* [(new) race_mouse.py](https://github.com/bnoleto/freePie_scripts/blob/master/race_mouse.py): Allows you to use the mouse to precisely control the steering in racing games, plus some key assignments for smooth acceleration. Works incredibly nice in games such as F1 2017 and simulators such as Project Cars. Although it is really painful assigning the axis within these games, the results are almost perfect.
  * *Hint: Put your mouse at 1600dpi-3200dpi for optimal performance. In my case, 1600dpi is great in Project Cars, while 3200dpi is very good in F1 2017. Use the LEFT MOUSE BUTTON to accelerate, and the RIGHT MOUSE BUTTON to brake. If you do any of these commands while holding the LSHIFT key, the axis increment/decrement rate will be faster, and if you do that holding the LCTRL key, the the axis increment/decrement rate will be slower. The steering sensitivity never changes.*
* [(new) race_xone.py](https://github.com/bnoleto/freePie_scripts/blob/master/race_xone.py): Almost the same as race_ds3, but I tried some tweaking to take advantage of the precision of the Xbox One controller. I don't know exactly why I did this.
* [xplane.py](https://github.com/bnoleto/freePie_scripts/blob/master/xplane.py): Script with center reduction on all axis. The left Analog Y axis is used for throttle purposes in flight simulators.
## Useful links
* scpToolkit - https://github.com/nefarius/ScpToolkit
* freePIE - https://github.com/AndersMalmgren/FreePIE
* vJoy - http://vjoystick.sourceforge.net
