import urllib2

def openAPI():
    url = "http://www.volunteermatch.org/api/call?action=helloWorld&query=%s"%("\"{\"name\":\"john\"}\"")
    print url
    u = urllib2.urlopen(url).read()
    print u

openAPI()
