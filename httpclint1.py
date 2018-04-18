import http.client

h=http.client.HTTPConnection("www.infiniteskills.com")
h.request("GET","/")
data = h.getrequest()
print(data.code)
print(data.headers)
text = data.readlines()
for t in text:
    print(t.decade('utf-8'))
