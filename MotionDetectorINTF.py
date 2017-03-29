import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template

import json


with open('settings.json') as settings_file:    
    settings = json.load(settings_file)

#start the websocket server
def startServer(msgHandler):
	
	class WSHandler(tornado.websocket.WebSocketHandler):
		
		def check_origin(self, origin):
			return True

		def open(self):
			print('connection opened...')
			#self.write_message("The server says: 'Hello'. Connection was accepted.")

		def on_message(self, message):
			handleMsg(self, message, msgHandler)

		def on_close(self):
			print('connection closed...')
			
	application = tornado.web.Application([
	  (r'/', WSHandler),
	])
	application.listen(settings['MDWebsocketPort'])
	tornado.ioloop.PeriodicCallback(try_exit, 1000).start() #for dev exit in terminal
	tornado.ioloop.IOLoop.instance().start()
	
def handleMsg(self, message, callback):
	
	data = json.loads(message)
	
	type, output = callback(data)
	if type == "status":
		self.write_message('{"name" : "MDStatus", "output": '+ str(output) + '}')
	elif type == "data":
		self.write_message('{"name" : "MDOutput", "output": '+ str(output) + '}')
	
	#bufferData[curser] = parsed_json['input']
	

#this is just for dev, to close the server in terminal
is_closing = False
def try_exit(): 
    global is_closing
    if is_closing:
        # clean up here
        tornado.ioloop.IOLoop.instance().stop()
        logging.info('exit success')


