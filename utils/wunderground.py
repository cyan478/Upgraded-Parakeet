import urllib2, json, datetime

def getKey():
    f = open('apikeys.txt','r').read()
    csv = f.split('\n')
    wu = csv[1].split(',')
    return wu[1]

APIkey = getKey()
url = "http://api.wunderground.com/api/%s/" % (APIkey)
query = "geolookup/conditions/forecast10day/q/"

def wuCall(year, month, day):
	currDay = datetime.datetime.now().toordinal()
	dayOfEvent = datetime.date(year, month, day).toordinal()
	if (dayOfEvent - currDay >= 10):
		return "The event is still too far away. Come back later, please!"
	u = urllib2.urlopen(url+query)
	json_string = u.read()
	parsed_json = json.loads(json_string)
	retStr = ""
	if 'location' in parsed_json.keys():
		location = parsed_json['location']['city']
		retStr += "In %s, \n " % (location)
	if (dayOfEvent - currDay == 0):
		temp_f = parsed_json['current_observation']['temp_f']
		weather = parsed_json['current_observation']['weather']
		cond = parsed_json['forecast']['simpleforecast']['forecastday'][0]['conditions']
		highTemp = parsed_json['forecast']['simpleforecast']['forecastday'][0]['high']['fahrenheit']
		lowTemp = parsed_json['forecast']['simpleforecast']['forecastday'][0]['low']['fahrenheit']
		retStr += "Current temperature: %s \n Weather: %s \n Forecasted condition: %s \n High temperature: %s \n Low temperature: %s" % (temp_f, weather, cond, highTemp, lowTemp)
	else:
		cond = parsed_json['forecast']['simpleforecast']['forecastday'][dayOfEvent - currDay]['conditions']
		highTemp = parsed_json['forecast']['simpleforecast']['forecastday'][dayOfEvent - currDay]['high']['fahrenheit']
		lowTemp = parsed_json['forecast']['simpleforecast']['forecastday'][dayOfEvent - currDay]['low']['fahrenheit']
		retStr += "Forecasted condition: %s \n High temperature: %s \n Low temperature: %s" % (cond, highTemp, lowTemp)
	#print parsed_json['forecast']['simpleforecast']['forecastday'][0]['date']['day']
	return retStr
	u.close()
	
def location(state, city):
	global query
	query += state + "/" + city + ".json"
	
def zipcode(zip):
	global query
	query += zip + ".json"

#location("NY", "Brooklyn")	
#zipcode("90210")
#print wuCall(15,1)
