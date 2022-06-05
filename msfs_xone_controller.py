import locale
from time import *

if starting:

	debug = True
	
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
	elevator_trim = AXIS_CENTER
	rudder_trim = AXIS_CENTER
	
	cond = 0
	
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
	
	elevator_trim_mode = False
	ground_mode = False
	
	button_pressed_before = False
	button_pressed_current = False
	
	button_pressed = None
	
	nextEpoch = 0

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
	
	def extend(axis,sec_axis):
	
		if axis == 0:
			signal_primary = 1
		else:
			signal_primary = axis/abs(axis)
		
		if sec_axis == 0:
			signal_secondary = 1
		else:
			signal_secondary = sec_axis/abs(sec_axis)
	
		difference = abs(abs(axis)-abs(sec_axis))
		
		return limit(signal_primary*(abs(axis)*(1 + ((AXIS_MAX-difference)/AXIS_MAX))), AXIS_MIN, AXIS_MAX)
		
	
	def toPress(axis):
		global nextEpoch
		if(epoch > nextEpoch and axis >= 0.1):
			nextEpoch = epoch + (1/(axis*0.01))
			return True
		else:
			return False
			
# loop começa aqui

epoch = round(time() * 1000)

# button assignments

v.setButton(1,pad.x)
v.setButton(2,pad.leftShoulder)
v.setButton(3,pad.rightShoulder)

v.setButton(4,pad.back)
v.setButton(5,pad.start)
v.setButton(6,pad.rightThumb)
v.setButton(7,pad.y)
v.setButton(8,pad.b)

button_pressed_current = (pad.x or pad.a)

elevator_trim_mode = pad.down

if(pad.x):
	thrust = AXIS_CENTER

if(elevator_trim_mode):
	pitch = AXIS_CENTER
	elevator_trim = limit(elevator_trim + (convert(apply_deadzone(pad.leftStickY,0.1))/250), AXIS_MIN, AXIS_MAX)
	#rudder_trim = limit(rudder_trim + (convert(apply_deadzone(-pad.leftTrigger+pad.rightTrigger,0.1))/250), AXIS_MIN, AXIS_MAX)
	#v.setButton(9,toPress(pad.rightTrigger))
	#v.setButton(0,toPress(pad.leftTrigger))

if(button_pressed_before and not button_pressed_current):
	if(button_pressed == "a"):
		ground_mode = not ground_mode

		if(ground_mode):
			diagnostics.notify("Ground Mode","Activated")
			#speech.say(GROUNDMODE_STRING + " " +ENABLED_STRING+".")
		else:
			diagnostics.notify("Ground Mode","Deactivated")
			#speech.say(GROUNDMODE_STRING + " " +DISABLED_STRING+".")
			
			
	button_pressed_before = False

if(pad.x or pad.a):
	if(pad.x):
		button_pressed = "x"
	else:
		button_pressed = "a"
		
	button_pressed_before = True

roll = convert(apply_deadzone(pad.leftStickX, 0.1))
if not elevator_trim_mode:
	pitch = convert(apply_deadzone(pad.leftStickY, 0.1))
yaw = convert(apply_deadzone((-pad.leftTrigger+pad.rightTrigger),0.1))

thrust = limit(thrust + (convert(apply_deadzone(pad.rightStickY,0.1))/250), AXIS_CENTER, AXIS_MAX)

# associação dos eixos

if(ground_mode):
	v.slider = convert(apply_deadzone(pad.leftTrigger, 0.1))
	v.dial = convert(apply_deadzone(pad.rightTrigger, 0.1))
	
	v.x = AXIS_CENTER
	v.z = roll
else:

	v.slider = AXIS_CENTER
	v.dial = AXIS_CENTER

	v.x = extend(roll,pitch)
	v.z = yaw

v.y = extend(pitch,roll)

v.rx = elevator_trim
v.ry = thrust
v.rz = rudder_trim

if (debug):

	diagnostics.watch(v.x)
	diagnostics.watch(epoch)
	diagnostics.watch(v.y)
	diagnostics.watch(pitch)
	diagnostics.watch(v.z)
	diagnostics.watch(v.rx)
	diagnostics.watch(v.ry)
	diagnostics.watch(v.rz)
	diagnostics.watch(v.slider)
	diagnostics.watch(v.dial)
	diagnostics.watch(elevator_trim_mode)
	diagnostics.watch(ground_mode)