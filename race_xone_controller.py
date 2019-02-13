if starting:
	system.setThreadTiming(TimingTypes.HighresSystemTimer)
	system.threadExecutionInterval = 0.5

	def reducao(entrada):
		reducao_centro = 45.0
		if entrada >= 0:
			return reducao_centro ** (1-(entrada/16383))
		else:
			return reducao_centro ** (1-(entrada/-16383))
	
	def reducao2(entrada):
		coeficiente = 2
		return 1
	
	v = vJoy[0]
	#j = joystick[1]
	pad = xbox360[0]
	
	clock = 0
	contador = 0

# laço de funcionamento começa aqui

eixoX = ((pad.leftStickX*16383)/reducao(pad.leftStickX*16383))
eixoY = ((pad.leftStickY*16383)/reducao(pad.leftStickY*16383))	

if pad.leftStickX > 0.7:
	eixoX = ((0.7*16383)/reducao(0.7*16383))
if pad.leftStickX < -0.7:
	eixoX = ((-0.7*16383)/reducao(-0.7*16383))
	
if pad.leftStickY > 0.7:
	eixoY = ((0.7*16383)/reducao(0.7*16383))
if pad.leftStickY < -0.7:
	eixoY = ((-0.7*16383)/reducao(-0.7*16383))
	
eixoRx = ((pad.rightStickX*16383)/reducao(pad.rightStickX*16383))
eixoRy = ((pad.rightStickY*16383)/reducao(pad.rightStickY*16383))
#eixoZ = ((j.z*16.383)/reducao(j.z*16.383))
acelerador = pad.rightTrigger*16383
freio = pad.leftTrigger*16383

# associação dos eixos

v.x = eixoX
v.y = -eixoY
v.rx = eixoRx
v.ry = eixoRy
#v.z = -eixoZ

v.slider = freio
v.dial = acelerador

#v.setButton(0,j.getDown(0))
#v.setButton(1,j.getDown(1))
#v.setButton(2,j.getDown(2))
#v.setButton(3,j.getDown(3))
#v.setButton(4,j.getDown(4))
#v.setButton(5,j.getDown(5))
#v.setButton(6,j.getDown(6))
#v.setButton(7,j.getDown(7))
#v.setButton(8,j.getDown(8))
#v.setButton(9,j.getDown(9))

# debugging

diagnostics.watch(pad.leftStickX)
diagnostics.watch(pad.leftTrigger)
diagnostics.watch(eixoX)
diagnostics.watch(eixoY)
diagnostics.watch(pad.rightTrigger)
diagnostics.watch(clock)
diagnostics.watch(v.x)
diagnostics.watch(v.z)
diagnostics.watch(v.y)
diagnostics.watch(v.rx)
diagnostics.watch(v.rz)
diagnostics.watch(reducao(v.x))