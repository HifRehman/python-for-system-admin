import urllib.request
# print(dir(urllib))
request_url = urllib.request.urlopen('https://www.google.com/')
print(request_url.read())



