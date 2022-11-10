from flask import render_template, request, redirect, request, session

def login():
    return render_template('login.html')

def verfiyCredentails():
    username = request.form['username']
    password = request.form['password']
    if username == '' and password == '':
        return redirect('/login?error=Fields cannot be empty')
    if username == 'admin' and password == 'password':
        session['username'] = username
        return redirect('/dashboard', code=302)
    return redirect('/login?error=Invalid Credentials', code=302)

def logout():
    session.pop('username', None)
    return redirect('/login')

def checkUserLoggedIn():
    if 'username' not in session:
        return False
    return True