import urllib2
import json

def wuTest():
    apikey = "1"
    url = "http://api.wunderground.com/api/%s/planner_12081209/q/CA/San_Francisco.json/q/NY/New_York.json"%(apikey)
    u = urllib2.urlopen(url)
    jsLoaded = json.loads(u.read())
    u.close()
    print jsLoaded
    

wuTest()
