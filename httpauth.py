import httplib
import base64
import string

h="172.30.42.127"
u="mg"
p="P4ssw0rd"

authtoken = base64.encodestring('%s:%s'%(u,p)).replace('\n','')
print(authtoken)

req = httplib.HTTP(h)
req.putrequest("GET","/protected/index.html")
req.putheader("Host",h)
req.putheader("Authorization","Basic %s" %authtoken)
req.endheaders()
req.send("")

statusCode, statusMsg, headers = req.getreply()

print("Response:",statusMsg)
