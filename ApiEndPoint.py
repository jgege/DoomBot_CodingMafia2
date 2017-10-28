import requests, json

class ApiEndPoint(object):
	def __init__(self, host):
		self.host = host

	def get(self, uri, data=""):
		if (len(data) > 0):
			payload = json.dumps(data)
			return requests.get(self.host + uri, data=payload).content
		return json.loads(requests.get(self.host + uri).content)
	
	def post(self, uri, data):
		payload = json.dumps(data)
		headers = {
	        'content-type': "application/json",
	        'cache-control': "no-cache"
	    }
		content = requests.post(self.host + uri, data=payload, headers=headers).content

		if (len(content) > 0):
			return json.loads(content)
		
		return None
