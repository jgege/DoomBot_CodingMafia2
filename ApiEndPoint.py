class ApiEndPoint(object):
	def __init__(self, connection):
		self.conn = connection

	def sendRequest(self, method, url):
		self.conn.request(method,url)
		res = self.conn.getresponse()
		return res.read()
