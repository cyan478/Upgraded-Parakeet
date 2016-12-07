import urllib2
from urllib import urlencode
from os import urandom
from hashlib import sha1, sha256
import datetime
import urllib2

def tmTest():
    apikey = "1"
    url = "https://app.ticketmaster.com/discovery/v2/events.json?apikey=%s"%(apikey)
    u = urllib2.urlopen(url).read()
    print u

tmTest()
