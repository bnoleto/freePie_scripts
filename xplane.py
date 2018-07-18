if starting:
	system.setThreadTiming(TimingTypes.HighresSystemTimer)
	system.threadExecutionInterval = 5
	def reducao(entrada):
		reducao_centro = 1.0
		if entrada >= 0:
			return reducao_centro ** (1-(entrada/int32_max))
		else:
			return reducao_centro ** (1-(entrada/int32_min))
	
	def reducao2(entrada):
		coeficiente = 5.0
		entrada += 16383
		return coeficiente ** (1-(entrada/16383))
	
	int32_max = (2 ** 14) - 1
	int32_min = (( 2** 14) * -1) + 1

	v = vJoy[0]
	pad = xbox360[0]
	
	acelerador = int32_min
	reverso = int32_min
	
	contador = 0
	
	modoReverso = False
	modoGround = False

# laço de funcionamento começa aqui

contador = contador + 1

if(modoReverso == False and modoGround == False and pad.x and pad.a and contador > 400):
	modoReverso = True
	acelerador = int32_max
	v.ry = int32_min
	v.rz = int32_min
	
	modoGround = True
	speech.say("Freios e reversos ligados.")
	contador = 0

elif(modoReverso == True and modoGround == True and pad.x and pad.a and contador > 400):
	modoReverso = False
	modoGround = False
	
	v.slider = int32_min
	v.dial = int32_min
	
	acelerador = int32_min
	v.ry = int32_min
	v.rz = int32_min
	
	speech.say("Freios e reversos desativados.")
	contador = 0
	
elif(modoReverso == False and pad.x and contador > 400):
	modoReverso = True
	acelerador = int32_max
	v.ry = int32_min
	v.rz = int32_min
	speech.say("Reverso em funcionamento.")
	contador = 0
elif(modoReverso == True and pad.x == True and contador > 400):
	modoReverso = False
	acelerador = int32_min
	v.ry = int32_min
	v.rz = int32_min
	speech.say("Reverso desativado.")
	contador = 0

if(modoGround == False and pad.a and contador > 400):
	modoGround = True
	speech.say("Freios em funcionamento")
	contador = 0

elif(modoGround == True and pad.a == True and contador > 400):
	modoGround = False
	v.slider = int32_min
	v.dial = int32_min
	speech.say("Freios desativados.")
	contador = 0

# lógica das manetes

reverso = -1*acelerador

if pad.rightStickY < -0.1 or pad.rightStickY > 0.1:
	acelerador = int(acelerador + pad.rightStickY*163.83)

eixoX = ((pad.leftStickX*16383)/reducao(pad.leftStickX*16383))
eixoY = ((pad.leftStickY*16383)/reducao(pad.leftStickY*16383))
eixoZ = (((-pad.leftTrigger+pad.rightTrigger)*16383)/reducao((-pad.leftTrigger+pad.rightTrigger)*16383))
eixoRx = ((pad.rightStickX*16383)/reducao(pad.rightStickX*16383))
eixoRy = reverso

if(eixoX > 13000):
	eixoX = 13000
	
if(eixoZ < -16000):
	eixoZ = -16000

if(acelerador > int32_max):
	acelerador = int32_max
elif(acelerador < int32_min):
	acelerador = int32_min

# associação dos eixos

v.x = eixoX
v.y = eixoY
v.z = eixoZ
v.rx = eixoRx

if(modoReverso):
	if pad.rightStickY < -0.1 or pad.rightStickY > 0.1:
		v.ry = reverso
		v.rz = int32_min
else:
	v.rz = acelerador
	v.ry = int32_min

if(modoGround):
	v.slider = (((pad.leftTrigger)*16383)/reducao(pad.leftTrigger*16383))
	v.dial = (((pad.rightTrigger)*16383)/reducao(pad.rightTrigger*16383))
	v.z = eixoX
else:
	v.z = eixoZ
	v.slider = int32_min
	v.dial = int32_min

# debugging

diagnostics.watch(v.x)
diagnostics.watch(v.y)
diagnostics.watch(v.z)
diagnostics.watch(v.rz)
diagnostics.watch(v.ry)
diagnostics.watch(v.slider)
diagnostics.watch(v.dial)
diagnostics.watch(modoReverso)
diagnostics.watch(modoGround)