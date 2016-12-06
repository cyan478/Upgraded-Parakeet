from sqlite3 import connect
import datetime

f = "../data/hangout.db"

def addFriend(initiator, friend):
    db = connect(f)
    c = db.cursor()
    try:
        c.execute("SELECT * FROM friends")
    except:
        c.execute("CREATE TABLE friends (initiator TEXT, friend TEXT, status TEXT, date INT)")
    query = "INSERT INTO friends VALUES (?, ?, ?, ?)"
    now = datetime.datetime.now()
    date = (now.month)*1000000 + (now.day)*10000 + now.year
    print date
    c.execute(query,(initiator, friend, "pending", date))
    db.commit()
    db.close()

def acceptReq(initiator, friend):
    db = connect(f)
    c = db.cursor()
    query = "UPDATE friends SET status=? WHERE initiator=? AND friend=?"
    c.execute(query, ("accepted", initiator, friend))
    db.commit()
    db.close()

def removeFriend(deletor, deleted):
    db = connect(f)
    c = db.cursor()
    query = "DELETE FROM friends WHERE initiator=? and friend=?"
    c.execute(query,(deletor,deleted))
    c.execute(query,(deleted,deletor))
    db.commit()
    db.close()

def listFriends(user):
    db = connect(f)
    c = db.cursor()
    query = "SELECT * FROM friends WHERE initiator=? or friend=?"
    sel=c.execute(query,(user,user))
    friends = []
    for record in sel:
        if record[0] == user:
            friends.append(record[1])
        else:
            friends.append(record[0])
        print record[2]
    db.commit()
    db.close()
    return friends

addFriend("elina","emma")
acceptReq("elina", "emma")
print listFriends("emma")
removeFriend("elina","emma")
print listFriends("emma")
