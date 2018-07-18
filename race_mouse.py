if starting:
	system.setThreadTiming(TimingTypes.HighresSystemTimer)
	system.threadExecutionInterval = 10

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
	
	def limitar(variavel):
		if variavel > 16383:
			return 16383
		elif variavel < -16383:
			return -16383
		else:
			return variavel
	
	def taxa_incremento(valorInicial, valorFinal,tempo):
		return ((abs(valorInicial)+abs(valorFinal))*10)/tempo
		
	def resetarEixo():
		return -5500

	v = vJoy[0]
	
	clock = 0
	contador = 0
	
	eixoX = 0
	acelerador = -16383
	
	tempoAcel = 500
	
	freio = -16383
	
	segundos = 0

# laço de funcionamento começa aqui

# contador em milésimos (ms)
contador += 10
if(contador >= 10000):
	contador = 0

eixoX += (int)(mouse.deltaX*1.6383)

if(keyboard.getKeyDown(Key.LeftControl)):
	tempoAcel = 1000
elif(keyboard.getKeyDown(Key.LeftShift)):
	tempoAcel = 250
else:
	tempoAcel = 500

if(mouse.leftButton):
	acelerador += taxa_incremento(-16383,16383,tempoAcel)
else:
	acelerador -= taxa_incremento(-16383,16383,tempoAcel)
	
if(mouse.rightButton):
	freio += taxa_incremento(-16383,16383,tempoAcel)
else:
	freio -= taxa_incremento(-16383,16383,tempoAcel)

if(mouse.middleButton):
	eixoX = resetarEixo()

eixoX = limitar(eixoX)
acelerador = limitar(acelerador)
freio = limitar(freio)

# associação dos eixos

v.x = eixoX
v.y = acelerador
v.z = freio

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

diagnostics.watch((int)(mouse.deltaX))
diagnostics.watch(eixoX)
diagnostics.watch(acelerador)
diagnostics.watch(contador)
diagnostics.watch(keyboard.getKeyDown(Key.LeftShift))
diagnostics.watch(mouse.leftButton)