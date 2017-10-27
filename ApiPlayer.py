from ApiEndPoint import ApiEndPoint

class ApiPlayer(ApiEndPoint):
	def __init__(self, connection):
		super(ApiPlayer, self).__init__(connection)
		
	def getInfo(self):
		return super(ApiPlayer, self).sendRequest("GET","/api/player")