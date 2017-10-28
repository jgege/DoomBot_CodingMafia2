import requests, json

class ApiEndPoint(object):
	def __init__(self, host):
		self.host = host

	def get(self, uri, data=""):
		if (len(data) > 0):
			payload = json.dumps(data)
			return requests.get(self.host + uri, data=payload).content
		return requests.get(self.host + uri).content

	def post(self, uri, data):
		payload = json.dumps(data)
		headers = {
	        'content-type': "application/json",
	        'cache-control': "no-cache"
	    }
		return requests.post(self.host + uri, data=payload, headers=headers).content
