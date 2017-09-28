if starting:
	system.setThreadTiming(TimingTypes.HighresSystemTimer)
	#system.threadExecutionInterval = 1

	def reducao(entrada):
		reducao_centro = 10.0
		if entrada >= 0:
			return reducao_centro ** (1-(entrada/int32_max))
		else:
			return reducao_centro ** (1-(entrada/int32_min))
	
	v = vJoy[0]
	j = joystick[1]

# laço de funcionamento começa aqui

eixoX = ((j.x*16.383)/reducao(j.x*16.383))
eixoY = ((j.y*16.383)/reducao(j.y*16.383))
eixoRx = ((j.xRotation*16.383)/reducao(j.xRotation*16.383))
eixoRy = ((j.yRotation*16.383)/reducao(j.yRotation*16.383))
eixoZ = ((j.z*16.383)/reducao(j.z*16.383))

# associação dos eixos

v.x = eixoX
v.y = eixoY
v.rx = eixoRx
v.ry = eixoRy
v.z = -eixoZ

# debugging

diagnostics.watch(j.getDown(0))
diagnostics.watch(j.y)
diagnostics.watch(v.x)
diagnostics.watch(v.z)
diagnostics.watch(v.y)
diagnostics.watch(v.rx)
diagnostics.watch(v.rz)
diagnostics.watch(reducao(v.x))
diagnostics.watch(j.xRotation*16.383)