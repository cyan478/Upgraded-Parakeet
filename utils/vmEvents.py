import urllib2
from urllib import urlencode
from os import urandom
from hashlib import sha1, sha256
import datetime
from base64 import b64encode

def openAPI():
    mom = datetime.datetime.now()
    now = str(mom.year)+"-"+str(mom.month)+"-"+str(mom.day)+"T"+str(mom.hour)+":"+str(mom.minute)+":"+str(mom.second)+"-"+str(mom.microsecond)
    nonce = b64encode(sha1(urandom(20)).digest())
    stuff = {
        "Username":"onCeen",
        "PasswordDigest": b64encode(sha256(nonce + str(now) + "87758c3cc7553fd0c6e69e5b3fca68f8").digest()), 
        "Nonce": nonce,
        "Created":now
    }
    dan = urlencode(stuff)
    url = "http://www.volunteermatch.org/api/call?UsernameToken&"
    url = url+str(dan)
    print url
    u = urllib2.urlopen(url).read()
    print u

def helloWorld():
    url = "http://www.volunteermatch.org/api/call?action=helloWorld&query=%s"%("{\"name\":\"john\"}")
    print url
    u = urllib2.urlopen(url).read()
    print u

openAPI()
helloWorld()
