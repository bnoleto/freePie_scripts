if starting:
	system.setThreadTiming(TimingTypes.HighresSystemTimer)
	system.threadExecutionInterval = 5
	
	v = vJoy[0]
	pad = xbox360[0]

	STEERING_SENSITIVITY = 0.1
	AXIS_RANGE = 1000

	AXIS_MIN = -AXIS_RANGE
	AXIS_MAX = AXIS_RANGE
	AXIS_CENTER = (AXIS_MIN+AXIS_MAX)/2
	
	WHEEL_MAX_DEGREES = 1080;
	
	WHEEL_THRESHOLD = 360;
	
	WHEEL_MAX_SIDE_DEGREES = WHEEL_MAX_DEGREES / 2;
	
	INCREMENT = 1
	CURRENT_INCREMENT = INCREMENT
	MAX_INCREMENT_MULTIPLIER = 50
	
	RSY_temp = 0

	def curve(input, max):
		
		current_max =  max ** 2
		current_signal = 1
		
		if( input == 0 ):
			current_signal = 1
		else:
			current_signal = input/abs(input)
		
		return ((current_signal * (input ** 2))/current_max)*max
	
	def limit(axis, lower_limit, upper_limit):
		if(axis > upper_limit):
			return upper_limit
		elif(axis < lower_limit):
			return lower_limit
		
		return axis
	
	def convert(input):
		
		return curve(input)*AXIS_RANGE
	
	def resetAxis():
		return 0
	
	axis_steering = AXIS_CENTER
	axis_accel = AXIS_CENTER
	axis_brakes = AXIS_CENTER
	axis_clutch = AXIS_CENTER
	axis_handbrake = AXIS_CENTER
	
	atingiu_limiar = False
	signal_limiar = 1

	def extend(axis,sec_axis,axis_local_min,axis_local_max):
	
		signal_primary = get_signal(axis)
		signal_secondary = get_signal(sec_axis)
	
		difference = abs(abs(axis)-abs(sec_axis))
		
		return limit(signal_primary*(abs(axis)*(1 + ((axis_local_max-difference)/axis_local_max))), axis_local_min, axis_local_max)

	def increment_function (axis_value, axis_range):
		return limit(CURRENT_INCREMENT + (abs(axis_value)/axis_range)*0.01,INCREMENT, MAX_INCREMENT_MULTIPLIER)
		
	def apply_deadzone (axis_value, min, max):
		
		signal = get_signal(axis_value)
		
		min_a = abs(min)
		max_a = abs(max)
		axis_value_a = abs(axis_value)

		return signal*((axis_value_a - min_a)/(max_a - min_a))

	def get_signal(number):
		if number == 0:
			return 1
		else:
			return number/abs(number)
		
### laço de funcionamento começa aqui ###

LSX = extend(pad.leftStickX,pad.leftStickY, -1, 1)
LSY = extend(pad.leftStickY, pad.leftStickX, -1, 1)
RSX = extend(pad.rightStickX,pad.rightStickY, -1, 1)
RSY = extend(pad.rightStickY, pad.rightStickX, -1, 1)

WHEEL_CURRENT_DEGREE = LSX*1000 / AXIS_MAX * WHEEL_MAX_SIDE_DEGREES

SIGNAL = get_signal (LSX)

if (abs(LSX) > 0):
	if (atingiu_limiar and abs(WHEEL_CURRENT_DEGREE) >= WHEEL_MAX_SIDE_DEGREES):
	
		CURRENT_INCREMENT = increment_function(LSX, 1)
		temp_steering = temp_steering + signal_limiar*CURRENT_INCREMENT
#		if (pad.leftStickX > 0.5):
#			temp_steering = temp_steering + signal_limiar*CURRENT_INCREMENT
#		else:
#			temp_steering = temp_steering - signal_limiar*CURRENT_INCREMENT
		
		axis_steering = limit((SIGNAL*WHEEL_THRESHOLD) + temp_steering, AXIS_MIN, AXIS_MAX)
#		if (abs(axis_steering) > 2):
#			if axis_steering == 0:
#				signal = 1
#			else:
#				signal = axis_steering/abs(axis_steering)
#			signal *= -1
#		
#			axis_steering = limit(axis_steering + signal*(2), AXIS_MIN, AXIS_MAX)
#		else:
#			axis_steering = limit(axis_steering + (convert(apply_deadzone(pad.leftStickX,0.1))/200), AXIS_MIN, AXIS_MAX)
		before_temp_steering = temp_steering
		if (SIGNAL <> signal_limiar or abs(LSX) <= 0):
			atingiu_limiar = False
			temp_steering = 0
			before_temp_steering = 0
			axis_steering = 0
			signal_limiar = SIGNAL
			CURRENT_INCREMENT = INCREMENT
	elif (abs(LSX*WHEEL_THRESHOLD) < WHEEL_THRESHOLD):
		atingiu_limiar = False
		temp_steering = 0
		before_temp_steering = 0
		axis_steering = 0
		signal_limiar = SIGNAL
		CURRENT_INCREMENT = INCREMENT
		
		axis_steering = curve(limit(LSX*(WHEEL_THRESHOLD*2), AXIS_MIN, AXIS_MAX), AXIS_MAX)
		
	else:
		atingiu_limiar = True
		signal_limiar = SIGNAL
		temp_steering = 0
		before_temp_steering = 0
		CURRENT_INCREMENT = INCREMENT
			
else:
	axis_steering = AXIS_CENTER




if (RSY > 0.2):

	RSY_temp = apply_deadzone(RSY, 0.2, 1)
	axis_accel = limit(RSY_temp*1000, AXIS_MIN, AXIS_MAX)
	
else:

	axis_accel = AXIS_CENTER
	
if (pad.leftTrigger > 0):

	axis_brakes = limit(pad.leftTrigger*1000, AXIS_MIN, AXIS_MAX)
	
else:

	axis_brakes = AXIS_CENTER
	
if (RSY < -0.1):

	RSY_temp = apply_deadzone(RSY, -0.1, -1)
	axis_clutch = limit(RSY_temp*1000, AXIS_MIN, AXIS_MAX)
	
else:

	axis_clutch = AXIS_CENTER
	
if (pad.rightTrigger > 0.1):

	axis_handbrake = limit(pad.rightTrigger*1000, AXIS_MIN, AXIS_MAX)
	
else:

	axis_handbrake = AXIS_CENTER

# associação dos eixos
v.x = axis_steering
v.y = axis_accel
v.z = axis_brakes
v.rx = axis_clutch * -1
v.ry = axis_handbrake

# associação dos botões

v.setButton(0, pad.leftShoulder)
v.setButton(1, pad.rightShoulder)
#v.setButton(0, pad.rightShoulder and axis_accel == 0)
#v.setButton(1, pad.rightShoulder and axis_accel <> 0)


# debugging

diagnostics.watch(v.y)
diagnostics.watch(increment_function(LSX, 1))
diagnostics.watch(INCREMENT)
diagnostics.watch((abs(LSX)/1)/MAX_INCREMENT_MULTIPLIER)
diagnostics.watch(abs(LSX)/1)
diagnostics.watch(abs(LSX))
diagnostics.watch(MAX_INCREMENT_MULTIPLIER)
#increment_value*((abs(axis_value)/axis_range)/MAX_INCREMENT_MULTIPLIER)

