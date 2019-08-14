import locale

if starting:
	
	system.setThreadTiming(TimingTypes.HighresSystemTimer)
	system.threadExecutionInterval = 5
	
	v = vJoy[0]
	pad = xbox360[0]
	
	AXIS_RANGE = 1000
	
	LANGUAGE = locale.getdefaultlocale()[0]
	
	AXIS_MIN = -AXIS_RANGE
	AXIS_MAX = AXIS_RANGE
	AXIS_CENTER = (AXIS_MIN+AXIS_MAX)/2

	thrust = AXIS_CENTER
	
	if(LANGUAGE == "pt_BR"):
		ENABLED_STRING = "ativado"
		DISABLED_STRING = "desativado"
		REVERSE_STRING = "reverso"
		GROUNDMODE_STRING = "modo solo"
		
	elif(LANGUAGE == "es_ES"):
		ENABLED_STRING = "activado"
		DISABLED_STRING = "desactivado"
		REVERSE_STRING = "reversor"
		GROUNDMODE_STRING = "modo suelo"
	
	else:		
		ENABLED_STRING = "enabled"
		DISABLED_STRING = "disabled"
		REVERSE_STRING = "reverse"
		GROUNDMODE_STRING = "ground mode"
	
	reverse_mode = False
	ground_mode = False
	
	button_pressed_before = False
	button_pressed_current = False
	
	button_pressed = None

	def curve(input):
		
		if(input < 0):
			return -(input ** 2)
		else:
			return input ** 2
	
	def convert(input):
		
		return curve(input)*AXIS_RANGE
	
	def limit(axis, lower_limit, upper_limit):
		if(axis > upper_limit):
			return upper_limit
		elif(axis < lower_limit):
			return lower_limit
		
		return axis
	
	def apply_deadzone(axis, value):
		if(axis >= -value and axis <= value):
			return AXIS_CENTER
		else:
			return axis

# loop começa aqui

button_pressed_current = (pad.x or pad.a)

if(button_pressed_before and not button_pressed_current):
	if(button_pressed == "x"):
		if(thrust >= -100 and thrust <= 100):
			reverse_mode = not reverse_mode
			thrust = AXIS_CENTER
			
			if(reverse_mode):
				speech.say(REVERSE_STRING + " " +ENABLED_STRING+".")
				
			else:
				speech.say(REVERSE_STRING + " " +DISABLED_STRING+".")
	if(button_pressed == "a"):
		ground_mode = not ground_mode

		if(ground_mode):
			speech.say(GROUNDMODE_STRING + " " +ENABLED_STRING+".")
		else:
			speech.say(GROUNDMODE_STRING + " " +DISABLED_STRING+".")
			
			
	button_pressed_before = False

if(pad.x or pad.a):
	if(pad.x):
		button_pressed = "x"
	else:
		button_pressed = "a"
		
	button_pressed_before = True
			
roll = convert(apply_deadzone(pad.rightStickX, 0.1))
pitch = convert(apply_deadzone(pad.rightStickY, 0.1))
yaw = convert(apply_deadzone((-pad.leftTrigger+pad.rightTrigger),0.1))

if(reverse_mode):
	thrust = limit(thrust + (convert(apply_deadzone(pad.leftStickY,0.1))/250), AXIS_MIN, AXIS_CENTER)
else:
	thrust = limit(thrust + (convert(apply_deadzone(pad.leftStickY,0.1))/250), AXIS_CENTER, AXIS_MAX)

# associação dos eixos

v.x = roll
v.y = pitch
v.z = yaw

if(reverse_mode):
	v.ry = AXIS_CENTER
	v.rz = -thrust
else:
	v.ry = thrust
	v.rz = AXIS_CENTER

if(ground_mode):
	v.slider = convert(apply_deadzone(pad.leftTrigger, 0.1))
	v.dial = convert(apply_deadzone(pad.rightTrigger, 0.1))
	v.x = AXIS_CENTER
	v.z = roll
else:
	v.x = roll
	v.z = yaw
	v.slider = AXIS_CENTER
	v.dial = AXIS_CENTER

# debugging
diagnostics.watch(v.x)
diagnostics.watch(v.y)
diagnostics.watch(pitch)
diagnostics.watch(v.z)
diagnostics.watch(v.ry)
diagnostics.watch(v.rz)
diagnostics.watch(v.slider)
diagnostics.watch(v.dial)
diagnostics.watch(reverse_mode)
diagnostics.watch(ground_mode)