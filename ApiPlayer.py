import requests
from ApiEndPoint import ApiEndPoint

class ApiPlayer(ApiEndPoint):
	def __init__(self, host):
		self.host = host

	def getInfo(self):
		return super(ApiPlayer, self).get("/api/player")

	def walkForward(self, steps):
		data = {"type" : "forward", "amount" : steps}
		return super(ApiPlayer, self).post("/api/player", data)
