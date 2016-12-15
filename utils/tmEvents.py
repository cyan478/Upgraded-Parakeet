import urllib2
import json
import userEvents

def getKey():
    f = open('apikeys.txt','r').read()
    csv = f.split('\n')
    tm = csv[0].split(',')
    return tm[1]

query = "&size=10&source=ticketmaster"
queryAddons = ""
apikey = getKey()
url = "https://app.ticketmaster.com/discovery/v2/events.json?apikey=%s"%(apikey)

"""
returns dict with keys:
'name' of event
'type' of event (to be used for user specifics)
'id' of event (to be used for user specifics)
'url' of link to ticketmaster event
'priceRange' (array of [currency, min, max])
'imgs' (array of dicts (dict has ratio, url, w, h, fallback(ignore)))
'note' (offered by the event) if one exists
"""
def tmCall(user):
    global query, queryAddons
    urlq = url+query+queryAddons
    u = urllib2.urlopen(urlq)
    queryAddons = ""
    j = json.load(u)
    types = userEvents.getEventTypes(user)
    for type in types:
        if len(type) > 0:
            tmClassType(type)
    events = []
    for elem in j["_embedded"]["events"]:
        if elem["name"] != "No Longer on Sale for Web":
            attempt = True
            try: #it should at least have these
                x = elem["_embedded"]["venues"][0]["location"]
                y = elem["_links"]["venues"]
            except: #don't get more info
                attempt = False
            if attempt:
                info = eventInfo(elem["id"])
                if info != {}:
                    events.append(info)
        
    u.close()
    json.dumps(j)
    return events

"""
returns dict for each venue with keys:
'city' = cityname (e.g Queens)
'zip' = zipCode
'country' = countryCode (e.g US)
'state' = stateCode (e.g NY)
'streetAddr' = street address (e.g 345 Chambers Street)
"""
def searchVen(venId):
    link = "https://app.ticketmaster.com/discovery/v2/venues/%s.json?apikey=%s"%(venId,apikey)
    u = urllib2.urlopen(link)
    j = json.load(u)

    dets = {}
    dets["city"] = j["name"]
    try:
        dets["zip"] = j["postalCode"]
    except:
        dets["zip"] = "00000"
    try:
        dets["state"] = j["state"]["stateCode"]
    except:
        try:
            inter = j["address"]["line2"].split()
            dets["state"] = inter[len(inter)-1]
        except:
            dets["state"] = ""
    dets["streetAddr"] = j["address"]["line1"]
    
    u.close()
    json.dumps(j)
    return dets

"""
returns dictionary of info about eventId with keys:
'type': type of event (e.g sports)
'name': name of event
'url': url of ticketmaster page for event
"""
def eventInfo(eventId):
    if eventId != "N/A":
        link = "https://app.ticketmaster.com/discovery/v2/events/%s.json?apikey=%s"%(eventId,apikey)
        try:
            u = urllib2.urlopen(link)
        except:
            return {}
        j = json.load(u)

        dets = {}
        #try:
        dets["id"] = j["id"]
        dets["name"] = j["name"]
        dets["url"] = j["url"]
        try:
            dets["date"] = j["dates"]["start"]["dateTime"]
        except:
            dets["date"] = "Date TBA"
        dets["latitude"] = j["_embedded"]["venues"][0]["location"]["latitude"]
        dets["longitude"] = j["_embedded"]["venues"][0]["location"]["longitude"]
        venId = j["_links"]["venues"][0]["href"].split("/")[4].split("?")[0]
        dets["venue"] = searchVen(venId)
        #except:
         #   return {}

        dets["type"] = j["classifications"][0]["segment"]["name"]
        eventImgs = []
        try: #not every event has a pleaseNote
            event["note"] = elem["pleaseNote"]
        except:
            pass
        try:
            for img in elem["images"]:
                eventImgs.append(img)
                event["imgs"] = eventImgs
        except:
            pass
        try:
            dets["priceRange"] = [
                j["priceRanges"][0]["currency"],
                j["priceRanges"][0]["min"],
                j["priceRanges"][0]["max"]
            ]
        except:
            dets["priceRange"] = ["N/A","N/A","N/A"]
        
        u.close()
        json.dumps(j)
        return dets

#===================QUERY ADDITION FXNS==================
def getQuery():
    return queryAddons

def tmKeyword(word):
    global queryAddons
    queryAddons += "&keyword=%s"%(word)

def tmStateCode(stateCode):
    global queryAddons
    queryAddons += "&stateCode=%s"%(stateCode)

def tmCode(post):
    global queryAddons
    queryAddons += "&postalCode=%s"%(post)

def tmCity(city):
    global queryAddons
    queryAddons += "&city=%s"%(city)

def tmClassType(type):
    global queryAddons
    queryAddons += "&classificationName=%s"%(type)

def tmStartDT(y, m, d):
    global queryAddons
    if (m<10):
        m = "0"+str(m)
    if (d<10):
        d = "0" + str(d)
    queryAddons += "&startDateTime=%s-%s-%sT01:01:00Z"%(y,m,d)

#only events starting after 2017-01-03 01:01
#tmStartDT(2017,01,03,01,01)
#tmCity("Queens")
#tmCode("11375")
#tmStateCode("NY")
#tmCall()
