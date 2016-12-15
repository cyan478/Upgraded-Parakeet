import datetime
from sqlite3 import connect

f = "data/hangout.db"

def createNotif(user,msg):
    db = connect(f)
    c = db.cursor()
    try:
        c.execute("SELECT * FROM notifs")
    except:
        c.execute("CREATE TABLE notifs (username TEXT, message TEXT, datetime TEXT)")
    query = "INSERT INTO notifs VALUES (?, ?, ?)"
    c.execute(query, (user, msg, datetime.datetime.now()))
    db.commit()
    db.close()

def getNotifs(user):
    db = connect(f)
    c = db.cursor()
    query = "SELECT message FROM notifs WHERE username=? ORDER BY datetime asc"
    try:
        sel = c.execute(query, (user,))
    except:
        c.execute("CREATE TABLE notifs (username TEXT, message TEXT, datetime TEXT)")
        sel = c.execute(query, (user,))
    notifs = []
    for msg in sel:
        notifs.append(msg[0])
    db.commit()
    db.close()
    return notifs

def removeNotif(user, msg):
    db = connect(f)
    c = db.cursor()
    query = "DELETE FROM notifs WHERE username=? AND message=?"
    c.execute(query, (user,msg))
    db.commit()
    db.close()

#createNotif("emmaV", "glinda added you as a connect!")
#print getNotifs("emmaV")
#removeNotif("emmaV", "glinda added you as a connect!")
#print getNotifs("emmaV")
