import tmEvents
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

def listEvents(user):
    db = connect(f)
    c = db.cursor()
    query = "SELECT * FROM users WHERE username=?"
    sel = c.execute(query, (user,))
    events = []
    for record in sel:
        userEvs = sel[5].split("-")
        for ev in userEvs:
            info = tmEvents.eventInfo(ev)
            add = {}
            add['name'] = info['name']
            add['url'] = info['url']
            events.append(info)
    return events
