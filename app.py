from flask import Flask, session, request, url_for, redirect, render_template
#from utils import authenticate
app = Flask(__name__)
app.secret_key = "deal with this later"

#======================================================================================= ROOT
@app.route("/")
def root():
    if( 'username' in session.keys() ):
        return redirect(url_for( 'mainpage' ))
    else:
        return redirect(url_for( 'login' ))
        
#====================================================================================== LOGIN
@app.route("/login/")
def login( **keyword_parameters ):
    message = ""
    if( 'message' in keyword_parameters):
        message = keyword_parameters['message']
    elif( 'message' in request.args ):
        message = request.args.get('message')
    return render_template('login.html', message = message)

#======================================================================= AUTHENTICATING LOGIN
@app.route("/authenticate/", methods = ["POST"] )
def authen():
    dbData = authenticate.dbHandler( )
    userNames = dbData['usernames']
    passWords = dbData['passwords']
    if request.form['account'] == 'Login':
        val = authenticate.authenticate(request.form, userNames, passWords )
        if val == True :
            session['username'] = request.form['user']
            return redirect(url_for('root'))
        else:
            return redirect(url_for('login', message = val))
    elif request.form['account'] == 'Register':
        val = authenticate.register(request.form, userNames, passWords)
        if val == True :
            return redirect(url_for('login', message = "Registration Successful"))
        else:
            return redirect(url_for('login', message = val))
    else:
        return redirect(url_for( 'root' ) )

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
#===================================================================================== LOGOUT
@app.route("/logout/")
def logout():
    session.pop('username')
    return redirect(url_for('root'))

if __name__ == "__main__":
    app.debug = True
    app.run()
