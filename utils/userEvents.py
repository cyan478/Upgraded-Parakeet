import tmEvents, notifs
from sqlite3 import connect

f = "data/hangout.db"

def addEvent(user, eventid):
    db = connect(f)
    c = db.cursor()
    info = tmEvents.eventInfo(eventid) #type, name, url RN
    query = "SELECT * FROM users WHERE username=?"
    sel = c.execute(query, (user,))
    for record in sel:
        idList = record[5]
        if (idList != ""):
            idList += "-%s"%(eventid)
        else:
            idList += "%s"%(eventid)
        query = "UPDATE users SET eventIdList=? WHERE username=?"
        c.execute(query, (idList, user))

        types = record[6]
        if (types != ""):
            types += "-%s"%(info["type"])
        else:
            types += "%s"%(info["type"])
        query = "UPDATE users SET types=? WHERE username=?"
        c.execute(query, (types,user))
    db.commit()
    db.close()

def getEventTypes(user):
    db = connect(f)
    c = db.cursor()
    #get user types
    query = "SELECT * FROM users WHERE username=?"
    sel = c.execute(query, (user,))
    types = []
    for record in sel:
        types = record[5].split("-")
    db.commit()
    db.close()
    return types

def listEvents(user):
    db = connect(f)
    c = db.cursor()
    query = "SELECT * FROM users WHERE username=?"
    sel = c.execute(query, (user,))
    events = []
    for record in sel:
        userEvs = record[4].split("-")
        print "userEvs" + str(userEvs)
        for ev in userEvs:
            info = tmEvents.eventInfo(ev)
            if info is not None and info.keys() != []:
                add = {}
                print "KEYS: " + str(info.keys())
                add['name'] = info['name']
                add['url'] = info['url']
                events.append(info)
    print events
    return events
    
def inviteFriends(user, friend, event):
  notifs.createNotif(friend, "%s has invited you to %s!" %(user, event))
