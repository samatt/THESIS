from OSC import OSCClient, OSCMessage

class oscSender(object):

	def __init__(self,port):
		self.client = OSCClient()
		self.client.connect( ("localhost", port) )
		print "Started server on port : " + str(port)

	def newNode(self,kind,args):
		
		if(kind == "Router"):
			self.client.send( OSCMessage("/new/Router", args ) )
		elif(kind == "Client"):
			self.client.send( OSCMessage("/new/Client", args ) )

	def updateNode(self,kind,args):
		
		if(kind == "Router"):
			self.client.send( OSCMessage("/update/Router", args ) )
		elif(kind == "Client"):
			self.client.send( OSCMessage("/update/Client", args ) )


	def removeNode(self,kind,args):
		
		if(kind == "Router"):
			self.client.send( OSCMessage("/remove/Router", args ) )
		elif(kind == "Client"):
			self.client.send( OSCMessage("/remove/Client", args ) )
