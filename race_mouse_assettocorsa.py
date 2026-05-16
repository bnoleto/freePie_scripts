if starting:
	
	import ctypes
	user32 = ctypes.windll.user32
	
	from ctypes import wintypes
	
	system.setThreadTiming(TimingTypes.HighresSystemTimer)
	system.threadExecutionInterval = 5
	
	class RECT(ctypes.Structure):
	    _fields_ = [
	        ("left", wintypes.LONG),
	        ("top", wintypes.LONG),
	        ("right", wintypes.LONG),
	        ("bottom", wintypes.LONG)
	    ]
	
	def get_increment_ratio():
		if(keyboard.getKeyDown(Key.LeftControl)):
			return 50*5
		elif(keyboard.getKeyDown(Key.LeftShift)):
			return 300*5
		else:
			return 100*5

	mouselock = False

	v = vJoy[0]

	STEERING_SENSITIVITY = 1
	AXIS_RANGE = 16384

	AXIS_MIN = -AXIS_RANGE
	AXIS_MAX = AXIS_RANGE
	AXIS_CENTER = (AXIS_MIN+AXIS_MAX)/2

	def limit(axis, lower_limit, upper_limit):
		if(axis > upper_limit):
			return round(upper_limit,3)
		elif(axis < lower_limit):
			return round(lower_limit,3)
		
		return round(axis,3)
	
	def resetAxis():
		return AXIS_CENTER
	
	wheel = AXIS_CENTER
	throttle = AXIS_MIN
	brakes = AXIS_MIN
	
	handbrake = AXIS_MIN
	clutch = AXIS_MIN
	
	rect = RECT(0, 0, 0, 0)
	
### laço de funcionamento começa aqui ###

if mouse.leftButton and not mouse.rightButton:
	throttle = limit(throttle + get_increment_ratio(), AXIS_MIN, AXIS_MAX)
	
	if(brakes > AXIS_MIN):
		#brakes = limit(brakes - 0.03, 0.0, 1.0)
		brakes = AXIS_MIN

elif mouse.rightButton and not mouse.leftButton:
	brakes = limit(brakes + get_increment_ratio(), AXIS_MIN, AXIS_MAX)
	
	if(throttle > AXIS_MIN):
		#throttle = limit(throttle - 0.03, 0.0, 1.0)
		throttle = AXIS_MIN

elif not mouse.leftButton and not mouse.rightButton:
	throttle = limit(throttle - get_increment_ratio(), AXIS_MIN, AXIS_MAX)
	brakes = limit(brakes - get_increment_ratio(), AXIS_MIN, AXIS_MAX)
else:
	throttle = limit(throttle + get_increment_ratio(), AXIS_MIN, AXIS_MAX)
	brakes = limit(brakes + get_increment_ratio(), AXIS_MIN, AXIS_MAX)
	
toggle_mouselock = mouse.middleButton

if toggle_mouselock:
    mouselock = not mouselock
if (mouselock):
    user32.ClipCursor(ctypes.byref(rect))
else:
	user32.ClipCursor(None)
	
wheel = limit(wheel + mouse.deltaX*STEERING_SENSITIVITY, AXIS_MIN, AXIS_MAX)
	
if(mouse.getButton(4)):
	#handbrake = limit(handbrake + 0.015, 0.0, 1.0)
	handbrake = AXIS_MAX
else:
	handbrake = limit(handbrake - (0.015*AXIS_RANGE), AXIS_MIN, AXIS_MAX)

if(keyboard.getKeyDown(Key.LeftAlt)):
	#clutch = limit(clutch + 0.015, 0.0, 1.0)
	clutch = AXIS_MAX
	if (mouse.leftButton):
		throttle = limit(throttle + get_increment_ratio(), AXIS_MIN, AXIS_MAX)
	else:
		throttle = AXIS_MIN
else:
	if throttle > AXIS_MIN:
		clutch = AXIS_MIN
	else:
		clutch = limit(clutch - (0.015*AXIS_RANGE), AXIS_MIN, AXIS_MAX)
	
# associação dos eixos
v.x = limit(wheel, AXIS_MIN, AXIS_MAX)
v.y = limit(throttle, AXIS_MIN, AXIS_MAX)
v.z = limit(brakes, AXIS_MIN, AXIS_MAX)

v.rx = limit(handbrake, AXIS_MIN, AXIS_MAX)
v.ry = limit(clutch, AXIS_MIN, AXIS_MAX)

v.setButton(0,mouse.wheelDown)
v.setButton(1,mouse.wheelUp)
v.setButton(2,mouse.getButton(3))
v.setButton(3,mouse.getButton(4))

v.setButton(4,keyboard.getKeyDown(Key.A))
v.setButton(5,keyboard.getKeyDown(Key.Z))
v.setButton(6,keyboard.getKeyDown(Key.P))
#v.setButton(6,keyboard.getKeyDown(Key.LeftAlt))
#v.setButton(7,keyboard.getKeyDown(Key.Space))

# debugging
diagnostics.watch(v.x)
diagnostics.watch(v.y)
diagnostics.watch(v.z)
diagnostics.watch(v.rx)
diagnostics.watch(v.ry)
