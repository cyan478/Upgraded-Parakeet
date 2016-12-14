import datetime

f = "data/hangout.db"

def createNotif(user,msg):
    db = connect(f)
    c = db.cursor()
    try:
        c.execute("SELECT * FROM notifs")
    except:
        c.execute("CREATE TABLE notifs (username TEXT, message TEXT, datetime TEXT")
    query = "INSERT INTO notifs VALUES (?, ?, ?)"
    c.execute(query, (user, msg, datetime.datetime.now()))
    db.commit()
    db.close()

def getNotifs(user):
    query = "SELECT msg FROM notifs WHERE username=? by datetime asc"
    sel = c.execute(query, (user,))
    notifs = []
    for msg in sel:
        notifs.append(msg[0])
    return notifs
