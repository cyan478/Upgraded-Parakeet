from flask import Flask, session, request, url_for, redirect, render_template
from utils import users, userEvents, connect
app = Flask(__name__)
app.secret_key = "deal with this later"

#======================================================================================= ROOT
@app.route("/")
def root():
    if( 'username' in session.keys() ):
        return redirect(url_for( 'home' ))
    else:
        return redirect(url_for( 'login' ))
        
#====================================================================================== LOGIN
@app.route("/login/")
def login():
    if "username" in session:
        return redirect(url_for('home'))
    return render_template('login.html')

#======================================================================= AUTHENTICATING LOGIN
@app.route("/authenticate/", methods=['POST'])
def authenticate():
    pw = request.form["password"]
    un = request.form["user"]
    em = request.form["email"]
    tp = request.form["account"]#login vs. register
    
    if tp == "Register":
        regRet = users.register(un,em,pw)#returns an error/success message
        return render_template('login.html', message = regRet)
        
    if tp == "Login":
        text = users.login(un,em,pw)#error message
        if text == "":#if no error message, succesful go back home
            session["username"] = un
            return redirect(url_for('home'))
        return render_template('login.html', message = text)

#============================================================= ALL EVENTS PAGE (AKA MAIN PAGE)
@app.route("/mainpage/")
def home():
    return render_template("main.html", user = session['username'])

#======================================================== CREATING A HANGOUT EVENT (INIVITING)
'''
@app.route("/create/")
def create():
    return render_template("create.html")
'''

#==================joinEvent=================
@app.route("/joinEvent/<id>")
def joinEvent(id):
    userEvents.addEvent(session['username'], id)
    return redirect( url_for('home') )

#========================userProfile=======================
@app.route("/user/<user>/")
def userProfile(user):
    friends = connect.listFriends(user)
    events = userEvents.listEvents(user)
    return render_template("profile.html", username = session['username'])

#===================================================================================== LOGOUT
@app.route("/logout/")
def logout():
    session.pop('username')
    return redirect(url_for('root'))

if __name__ == "__main__":
    app.debug = True
    app.run()
