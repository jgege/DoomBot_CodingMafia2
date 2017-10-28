import requests, json

class ApiEndPoint(object):
	def __init__(self, host):
		self.host = host

	def get(self, uri):
		return requests.get(self.host + uri).content

	def post(self, uri, data):
		payload = json.dumps(data)
		headers = {
	        'content-type': "application/json",
	        'cache-control': "no-cache"
	    }
		return requests.request("POST", self.host + uri, data=payload, headers=headers).text
