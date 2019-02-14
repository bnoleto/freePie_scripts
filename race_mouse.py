if starting:
	system.setThreadTiming(TimingTypes.HighresSystemTimer)
	system.threadExecutionInterval = 5
	
	v = vJoy[0]

	STEERING_SENSITIVITY = 0.2
	AXIS_RANGE = 1000

	AXIS_MIN = -AXIS_RANGE
	AXIS_MAX = AXIS_RANGE
	AXIS_CENTER = (AXIS_MIN+AXIS_MAX)/2

	def limit(axis, lower_limit, upper_limit):
		if(axis > upper_limit):
			return upper_limit
		elif(axis < lower_limit):
			return lower_limit
		
		return axis
	
	def resetAxis():
		return 0
	
	axis_x = AXIS_CENTER
	throttle = AXIS_CENTER
	brakes = AXIS_CENTER

# laço de funcionamento começa aqui

axis_x = limit(axis_x + (mouse.deltaX/1000)*STEERING_SENSITIVITY, -1.0, 1.0)

if(mouse.middleButton):
	axis_x = resetAxis()

if(keyboard.getKeyDown(Key.LeftControl)):
	increment_ratio = 0.005
elif(keyboard.getKeyDown(Key.LeftShift)):
	increment_ratio = 0.015
else:
	increment_ratio = 0.01

if(mouse.leftButton):
	throttle = limit(throttle + increment_ratio, 0.0, 1.0)
	brakes = limit(brakes - 0.015, 0.0, 1.0)
else:
	throttle = limit(throttle - increment_ratio, 0.0, 1.0)
	
if(mouse.rightButton):
	brakes = limit(brakes + increment_ratio, 0.0, 1.0)
	throttle = limit(throttle - 0.015, 0.0, 1.0)
else:
	brakes = limit(brakes - increment_ratio, 0.0, 1.0)

# associação dos eixos
v.x = limit(axis_x*AXIS_RANGE, AXIS_MIN, AXIS_MAX)
v.y = limit(throttle*AXIS_RANGE, AXIS_CENTER, AXIS_MAX)
v.z = limit(brakes*AXIS_RANGE, AXIS_CENTER, AXIS_MAX)

v.setButton(0,mouse.wheelDown)
v.setButton(1,mouse.wheelUp)
v.setButton(2,mouse.getButton(3))
v.setButton(3,mouse.getButton(4))

# debugging

diagnostics.watch(v.x)
diagnostics.watch(v.y)
diagnostics.watch(v.z)
