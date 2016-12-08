import urllib2
import json

APIkey = "1"
url = "http://api.wunderground.com/api/%s/" % (APIkey)
query = ""
def wuCall():
	u = urllib2.urlopen(url+query)
	json_string = u.read()
	parsed_json = json.loads(json_string)
	location = parsed_json['location']['city']
	temp_f = parsed_json['current_observation']['temp_f']
	print "Current temperature in %s is: %s" % (location, temp_f)
	u.close()

wuCall()
