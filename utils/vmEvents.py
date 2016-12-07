import urllib2
import datetime

query = "&size=20"
apikey = "1"
url = "https://app.ticketmaster.com/discovery/v2/events.json?apikey=%s"%(apikey)

def tmCall():
    u = urllib2.urlopen(url+query).read()
    print u

def tmKeyword(word):
    global query
    query += "&keyword=%s"(word)

def tmCode(post):
    global query
    query += "&postalCode=%s"(post)

def tmCity(city):
    global query
    query += "&city=%s"(city)

#def tmStartTime(str):
 #   global query
  #  query += "&startDateTime
#ALSO tmEndTime()


tmTest()
