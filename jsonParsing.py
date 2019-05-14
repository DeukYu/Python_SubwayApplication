import urllib
import json
import datetime

url =
u = urllib.urlopen(url)
data = json.load(u.read())
print(data)