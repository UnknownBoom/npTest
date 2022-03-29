import http.client
import time

conn = http.client.HTTPConnection("localhost", 8080)
payload = ''
headers = {}
for i in range(1000):
    n = time.time()
    conn.request("GET", "/", payload, headers)
    res = conn.getresponse()
    n = time.time() - n
    print(res.status)
    print(n)