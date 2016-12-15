import urllib2, json

def getKey():
    f = open('../apikeys.txt','r').read()
    csv = f.split('\n')
    di = csv[2].split(',')
    return di[1]



query=""

def directionsCall(origin, destination, mode):
  APIkey = getKey()
  url = "https://maps.googleapis.com/maps/api/directions/json?"
  query= "origin=%s" %(origin)
  u = urllib2.urlopen(url+query+APIkey)
  json_string = u.read()
  parsed_json = json.loads(json_string)
  for elem in parsed_json["routes"][0]["legs"][0]["steps"]:
    print elem["html_instructions"]
  
def origin(origin):
  global query
  query += "origin=%s" %(origin)
  
def destination(dest):
  global query
  query += "&destination=%s" %(dest)
  
def mode(mode):
  global query
  query += "&mode=%s" %(mode)
  
def key():
  global query
  query += "&key="

def directions(origin, destination, mode):
    directionsCall()

origin("2128+East+28th+St+Brooklyn")
destination("30+Rockefeller+Plaza+NY")
mode("walking")
key()
directionsCall()
