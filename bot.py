import httplib
conn = httplib.HTTPConnection("localhost:6001")
conn.request("GET","/api/player")
res = conn.getresponse()
print res.read()
print res.status, res.reason
