import urllib2, json

def getKey():
    f = open('apikeys.txt','r').read()
    csv = f.split('\n')
    di = csv[2].split(',')
    return di[1]


def directionsCall(dest, origin, mode):
  APIkey = getKey()
  url = "https://maps.googleapis.com/maps/api/directions/json?"
  query=""
  query += "origin=%s" %(origin)
  query += "&destination=%s" %(dest)
  query += "&mode=%s" %(mode)
  query += "&key="
  print query
  u = urllib2.urlopen(url+query+APIkey)
  json_string = u.read()
  parsed_json = json.loads(json_string)
  retstr=''
  for elem in parsed_json["routes"][0]["legs"][0]["steps"]:
      retstr+= elem["html_instructions"].replace('<b>','').replace('</b>','').replace('<div style="font-size:0.9em">','').replace('</div>','')+'\n'
  return retstr




