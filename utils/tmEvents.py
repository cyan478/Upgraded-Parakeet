import urllib2
import datetime
import json

query = ""
apikey = "997UMSmG0TC6AmayjR6p4B9TTEA9HO1i"
url = "https://app.ticketmaster.com/discovery/v2/events.json?size=20&apikey=%s"%(apikey)

def tmCall():
    urlq = url+query
    print urlq
    u = urllib2.urlopen(urlq)
    j = json.load(u)
    for elem in j["_embedded"]["events"]:
        print "What?: %s"%(elem["name"])
        print "More info: %s"%(elem["url"])
        try:
            print "Event's note: %s"%(elem["pleaseNote"])
        except:
            pass
        print ""

def tmKeyword(word):
    global query
    query += "&keyword=%s"%(word)

def tmCode(post):
    global query
    query += "&postalCode=%s"%(post)

def tmCity(city):
    global query
    query += "&city=%s"%(city)

def tmStartDT(y, m, d, hr, min):
    global query
    if (m<10):
        m = "0"+str(m)
    if (d<10):
        d = "0" + str(d)
    if (hr<10):
        hr = "0" + str(hr)
    if (min<10):
        min = "0" + str(min)
    query += "&startDateTime=%s-%s-%sT%s:%s:00Z"%(y,m,d,hr,min)

tmStartDT(2017,01,03,01,01)
tmCity("Queens")
tmCall()
