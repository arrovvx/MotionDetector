import MotionDetectorINTF as MD

#this function is called everytime a set of acc data is received
#return a command and the corresponding values
#e.g. "status", "done"
#e.g. "data", -10
#return a bad command and nothing will happen, but always return a tuple of 2

def handleData(Data):
	print(Data.shape)
	return "data", 10
	

	
#start the websocket server
MD.startServer(handleData)




#***Tell me if you need MongoDB storage functions***

