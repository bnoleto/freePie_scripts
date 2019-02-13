if starting:
	system.setThreadTiming(TimingTypes.HighresSystemTimer)
	system.threadExecutionInterval = 0.5

	def reducao(entrada):
		reducao_centro = 10.0
		if entrada >= 0:
			return reducao_centro ** (1-(entrada/16383))
		else:
			return reducao_centro ** (1-(entrada/-16383))
	
	def reducao2(entrada):
		coeficiente = 5.0
		entrada += 16383
		return coeficiente ** (1-(entrada/16383))
	
	v = vJoy[0]
	j = joystick[1]
	pad = xbox360[0]
	
	clock = 0
	contador = 0

# laço de funcionamento começa aqui

eixoX = ((j.x*16.383)/reducao(j.x*16.383))
eixoY = ((j.y*16.383)/reducao(j.y*16.383))
eixoRx = ((j.xRotation*16.383)/reducao(j.xRotation*16.383))
eixoRy = ((j.yRotation*16.383)/reducao(j.yRotation*16.383))
#eixoZ = ((j.z*16.383)/reducao(j.z*16.383))
acelerador = (((-1+pad.rightTrigger*2)*16383)/reducao2((pad.rightTrigger)*16383))
freio = (((-1+pad.leftTrigger*2)*16383)/reducao2(pad.leftTrigger*16383))

# associação dos eixos

v.x = eixoX
v.y = eixoY
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

diagnostics.watch(pad.leftTrigger)
diagnostics.watch(pad.rightTrigger)
diagnostics.watch(clock)
diagnostics.watch(j.getDown(0))
diagnostics.watch(j.z)
diagnostics.watch(v.x)
diagnostics.watch(v.z)
diagnostics.watch(v.y)
diagnostics.watch(v.rx)
diagnostics.watch(v.rz)
diagnostics.watch(reducao(v.x))
diagnostics.watch(j.xRotation*16.383)
diagnostics.watch(j.getDown(0))