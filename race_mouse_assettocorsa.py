if starting:
	from ctypes import *
	user32 = windll.user32

	system.setThreadTiming(TimingTypes.HighresSystemTimer)
	system.threadExecutionInterval = 5
	
	def get_increment_ratio():
		if(keyboard.getKeyDown(Key.LeftControl)):
			return 0.005
		elif(keyboard.getKeyDown(Key.LeftShift)):
			return 0.03
		else:
			return 0.01

	mouselock = False

	v = vJoy[0]

	STEERING_SENSITIVITY = 0.3
	AXIS_RANGE = 1000

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
		return 0
	
	axis_x = AXIS_CENTER
	throttle = AXIS_CENTER
	brakes = AXIS_CENTER
	
	handbrake = AXIS_CENTER
	clutch = AXIS_CENTER
	
### laço de funcionamento começa aqui ###

if mouse.leftButton and not mouse.rightButton:
	throttle = limit(throttle + get_increment_ratio(), 0.0, 1.0)
	
	if(brakes > 0):
		brakes = limit(brakes - 0.03, 0.0, 1.0)

elif mouse.rightButton and not mouse.leftButton:
	brakes = limit(brakes + get_increment_ratio(), 0.0, 1.0)
	
	if(throttle > 0):
		throttle = limit(throttle - 0.03, 0.0, 1.0)

elif not mouse.leftButton and not mouse.rightButton:
	throttle = limit(throttle - get_increment_ratio(), 0.0, 1.0)
	brakes = limit(brakes - get_increment_ratio(), 0.0, 1.0)
	
else:
	throttle = limit(throttle + get_increment_ratio(), 0.0, 1.0)
	brakes = limit(brakes + get_increment_ratio(), 0.0, 1.0)

toggle_mouselock = keyboard.getPressed(Key.M)

if toggle_mouselock:
    mouselock = not mouselock
if (mouselock):
    user32.SetCursorPos(0, 5000) # lock mouse at left-bottom of screen (x y pixel coordinates)

axis_x = limit(axis_x + (mouse.deltaX/1000)*STEERING_SENSITIVITY, -1.0, 1.0)

if(mouse.middleButton):
	axis_x = resetAxis()
	
if(keyboard.getKeyDown(Key.Space)):
	handbrake = limit(handbrake + 0.015, 0.0, 1.0)
else:
	handbrake = limit(handbrake - 0.015, 0.0, 1.0)

if(keyboard.getKeyDown(Key.LeftAlt)):
	clutch = limit(clutch + 0.015, 0.0, 1.0)
else:
	clutch = limit(clutch - 0.015, 0.0, 1.0)

# associação dos eixos
v.x = limit(axis_x*AXIS_RANGE, AXIS_MIN, AXIS_MAX)
v.y = limit(throttle*AXIS_RANGE, AXIS_CENTER+1, AXIS_MAX+1)
v.z = limit(brakes*AXIS_RANGE, AXIS_CENTER, AXIS_MAX)

v.rx = limit(handbrake*AXIS_RANGE, AXIS_CENTER, AXIS_MAX)
v.ry = limit(clutch*AXIS_RANGE, AXIS_CENTER, AXIS_MAX)

v.setButton(0,mouse.wheelDown)
v.setButton(1,mouse.wheelUp)
v.setButton(2,mouse.getButton(3))
v.setButton(3,mouse.getButton(4))

v.setButton(4,keyboard.getKeyDown(Key.A))
v.setButton(5,keyboard.getKeyDown(Key.Z))
#v.setButton(6,keyboard.getKeyDown(Key.LeftAlt))
#v.setButton(7,keyboard.getKeyDown(Key.Space))

# debugging
diagnostics.watch(v.x)
diagnostics.watch(v.y)
diagnostics.watch(v.z)
