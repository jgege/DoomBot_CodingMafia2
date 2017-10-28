import httplib, urllib
import requests
import json
import time

def getRequest( uri ):
   conn = httplib.HTTPConnection("localhost:6001")
   conn.request("GET", uri)
   return json.loads(conn.getresponse().read());

def postRequest( uri , payload):
    url = "http://localhost:6001" + uri
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text;


res = getRequest("/api/player")
print res

data = {"type" : "forward", "amount": 25}
res = postRequest("/api/player/actions", json.dumps(data))
print res

res = getRequest("/api/player")
print res['position']['x']

random = {
    "r" : "a",
    "n" : "d",
    "o" : "m"
    }
print json.dumps(random)
