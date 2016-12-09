import urllib2
import json

APIkey = "1"
url = "http://api.wunderground.com/api/%s/" % (APIkey)
query = "geolookup/conditions/forecast/q/"

def wuCall():
	u = urllib2.urlopen(url+query)
	json_string = u.read()
	parsed_json = json.loads(json_string) 
	location = parsed_json['location']['city']
	temp_f = parsed_json['current_observation']['temp_f']
	weather = parsed_json['current_observation']['weather']
	print "Current temperature and weather in %s is: %s and %s" % (location, temp_f, weather)
	u.close()
	
def location(state, city):
	global query
	query += state + "/" + city + ".json"
	
def zipcode(zip):
	global query
	query += zip + ".json"

#location("NY", "Brooklyn")	
zipcode("90210")
wuCall()
