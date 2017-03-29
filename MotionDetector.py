import MotionDetectorINTF as MD

#this function is called everytime there is a batch of data (400 default, can be changed in settings.json)
def handleData(Data):
	#print(Data.shape)
	print(Data)
	return 3
	

	
#start the websocket server
MD.startServer(handleData)




#***Tell me if you need MongoDB storage functions***

