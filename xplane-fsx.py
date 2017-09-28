if starting:
	system.setThreadTiming(TimingTypes.HighresSystemTimer)
	#system.threadExecutionInterval = 1

	def reducao(entrada):
		reducao_centro = 10.0
		if entrada >= 0:
			return reducao_centro ** (1-(entrada/int32_max))
		else:
			return reducao_centro ** (1-(entrada/int32_min))

	int32_max = (2 ** 14) - 1
	int32_min = (( 2** 14) * -1) + 1

	v = vJoy[0]
	j = joystick[1]

# laço de funcionamento começa aqui

if(acelerador > int32_max):
	acelerador = int32_max
elif(acelerador < int32_min):
	acelerador = int32_min

# lógica das manetes

if j.y < -100 or j.y > 100:
	acelerador = int(acelerador + (eixoY*-1)/200)

eixoX = ((j.x*16.383)/reducao(j.x*16.383))
eixoY = ((j.y*16.383)/reducao(j.y*16.383))
eixoZ = ((j.z*16.383)/reducao(j.z*16.383))
eixoRx = ((j.xRotation*16.383)/reducao(j.xRotation*16.383))
eixoRy = ((j.yRotation*16.383)/reducao(j.yRotation*16.383))

# associação dos eixos

v.x = eixoX
v.y = eixoY
v.z = -eixoZ
v.rx = eixoRx
v.ry = eixoRy
v.rz = acelerador

# debugging

diagnostics.watch(j.getDown(0))
diagnostics.watch(clock)
diagnostics.watch(acelerador)