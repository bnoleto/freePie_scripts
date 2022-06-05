if starting:
	
	system.setThreadTiming(TimingTypes.HighresSystemTimer)
	system.threadExecutionInterval = 5
	
	v = vJoyV2[0]
	pad = xinput[0]
	v.setController(pad.controllerHandle())
	