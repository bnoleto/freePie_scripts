if starting:

	system.setThreadTiming(TimingTypes.HighresSystemTimer)
	system.threadExecutionInterval = 5	
	
	x = 0
	y = 0
	
	padCursorEnabled = False
	
	pad = xbox360[0]
	
	val = 0
	
	def limit(axis, increment):
		return round(axis + increment*10, 0)
	
	initialPressingInterval = 40
	pressingInterval = 0


pressingInterval = pressingInterval+1

if (xbox360[0].start and pressingInterval >= 0) :
	padCursorEnabled = not padCursorEnabled

if (padCursorEnabled) :

	acceleration = ((-pad.leftShoulder+pad.rightShoulder)+1)/2
	
	if(abs(pad.rightStickX) > 0.1) :
		mouse.deltaX = x = pad.rightStickX*10

	if(abs(pad.rightStickY) > 0.1) :
		mouse.deltaY = y = -pad.rightStickY*10
		
	if (pressingInterval >= 0) :
		pressingInterval = -initialPressingInterval
		
		mouse.setButton(0,pad.a)
		mouse.setButton(1,pad.y)

diagnostics.watch(padCursorEnabled)
diagnostics.watch(x)
diagnostics.watch(y)
diagnostics.watch(val)