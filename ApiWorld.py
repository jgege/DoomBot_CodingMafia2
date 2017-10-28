import requests

class ApiWorld(object):
    def __init__(self, host):
        self.host = host
        
    def getInfo(self):
        return requests.get(self.host+"/api/world").content