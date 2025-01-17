import os
from flask import Flask, session, redirect, escape, request

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', default=None)

@app.route('/')

def index():

    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])

    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])

def login():

    if request.method == 'POST':

        session['username'] = request.form['username']
        return redirect('/')

    return '''
        <form method="post">
        <p><input type=text name=username>
        <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout', methods=['GET', 'POST'])

def logout():

    if request.method == "POST":
        session.pop('username', None)
        return redirect('/')

    return '''
        <form method="post">
        <p><input type=submit value=logout>
        </form>
    '''