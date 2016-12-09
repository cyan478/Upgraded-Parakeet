import urllib2
import datetime
import json

query = ""
apikey = "1" #DELETE BEFORE COMMITING
url = "https://app.ticketmaster.com/discovery/v2/events.json?size=1&apikey=%s"%(apikey)

#returns dict with keys:
#name of event
#type of event (to be used for user specifics)
#id of event (to be used for user specifics)
#url of link to ticketmaster event
#priceRange(array of [currency, min, max])
#imgs (array of dicts (dict has ratio, url, w, h, fallback(ignore)))
#note (offered by the event) if one exists
def tmCall():
    urlq = url+query
    u = urllib2.urlopen(urlq)
    j = json.load(u)
    events = []
    for elem in j["_embedded"]["events"]:
        event = {}
        event["venId"] = elem["_links"]["venues"][0]["href"].split("/")[4].split("?")[0]
        event["name"] = elem["name"]
        event["type"] = elem["classifications"][0]["segment"]["name"]
        event["id"] = elem["id"]
        event["url"] = elem["url"]
        event["priceRange"] = [
            elem["priceRanges"][0]["currency"],
            elem["priceRanges"][0]["min"],
            elem["priceRanges"][0]["max"]
        ]

        eventImgs = []
        for img in elem["images"]:
            eventImgs.append(img)
        event["imgs"] = eventImgs
        
        try: #not every event has a pleaseNote
            event["note"] = elem["pleaseNote"]
        except:
            pass
        events.append(event)
        
    u.close()
    json.dumps(j)
    for event in events:
        for key in event.keys():
            #5+5
            print "%s\n\t"%(key) + str(event[key])
        print "\n"
    return events

#===================QUERY ADDITION FXNS==================
def tmKeyword(word):
    global query
    query += "&keyword=%s"%(word)

def tmStateCode(stateCode):
    global query
    query += "&stateCode=%s"%(stateCode)

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

#only events starting after 2017-01-03 01:01
tmStartDT(2017,01,03,01,01)
tmCity("Queens")
tmCall()
