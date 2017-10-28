from ApiEndPoint import ApiEndPoint

class ApiPlayer(ApiEndPoint):
	def __init__(self, host):
		self.host = host

	def getInfo(self):
		return super(ApiPlayer, self).get("/api/player")

	def doAction(self, data):
		return super(ApiPlayer, self).post("/api/player/actions", data)

	def moveForward(self, amount):
		data = {"type" : "forward", "amount" : amount}
		return self.doAction(data)

	def moveBackward(self, amount):
		data = {"type" : "backward", "amount" : amount}
		return self.doAction(data)
	
	def turnLeft(self, amount):
		data = {"type" : "turn-left", "amount" : amount}
		return self.doAction(data)

	def turnRight(self, amount):
		data = {"type" : "turn-right", "amount" : amount}
		return self.doAction(data)
	
	def strafeLeft(self, amount):
		data = {"type" : "strafe-left", "amount" : amount}
		return self.doAction(data)	
		
	def strafeRight(self, amount):
		data = {"type" : "strafe-right", "amount" : amount}
		return self.doAction(data)	
	
	def switchWeapon(self, amount):
		data = {"type" : "switch-weapon", "amount": amount}
		return self.doAction(data)
	
	def shoot(self):
		data = {"type" : "shoot"}
		return self.doAction(data)
	
	def use(self):
		data = {"type" : "use"}
		return self.doAction(data)
