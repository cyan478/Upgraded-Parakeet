from sqlite3 import connect

f = "data/hangout.db"

def addFriend(initiator, friend):
    db = connect(f)
    c = db.cursor()
    try:
        c.execute("SELECT * FROM friends")
    except:
        c.execute("CREATE TABLE friends (initiator TEXT, friend TEXT")
    query = "INSERT INTO friends VALUES (?, ?)"
    c.execute(query,(initiator, friend))
    db.commit()
    db.close()

def findFriends(user):
    db = connect(f)
    c = db.cursor()

    #get user types
    query = "SELECT * FROM users WHERE username=?"
    c.execute(query, (user,))
    uTypes = []
    for record in sel:
        uTypes = record[6].split("-")

    #get other ppls types
    query = "SELECT * FROM users"
    sel = c.execute(query, (user,))
    users = []
    for record in sel:
        if record[0] == user:
            pass
        else:
            types = record[6].split("-")
            for type in types:
                if type in uTypes and user not in users:
                    users.append(record[0])
    db.commit()
    db.close()
    return users

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
    db.commit()
    db.close()
    return friends

""" for old fxnality
def acceptReq(initiator, friend):
    db = connect(f)
    c = db.cursor()
    query = "UPDATE friends SET status=? WHERE initiator=? AND friend=?"
    c.execute(query, ("accepted", initiator, friend))
    now = datetime.datetime.now()
    date = (now.month)*1000000 + (now.day)*10000 + now.year
    query = "UPDATE friends SET date=? WHERE initiator=? AND friend=?"
    c.execute(query, (date, initiator, friend))
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

def isFriendversary(friendA, friendB):
    db = connect(f)
    c = db.cursor()
    now = datetime.datetime.now()
    date = (now.month)*100 + (now.day)
    
    query = "SELECT * FROM friends WHERE initiator=? AND friend=?"
    sel = c.execute(query, (friendA, friendB))
    for record in sel: #where record[3] = date
        if record[3]/10000 == date:
            db.commit()
            db.close()
            return True
    sel = c.execute(query, (friendB, friendA))
    for record in sel:
        if record[3]/10000 == date:
            db.commit()
            db.close()
            return True
    db.commit()
    db.close()
    return False
"""
