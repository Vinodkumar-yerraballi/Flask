from datetime import timedelta

from flask import (Flask, flash, redirect, render_template, request, session,
                   url_for)

app = Flask(__name__)
app.secret_key = "vinod"
app.permanent_session_lifetime = timedelta(minutes=2)


@app.route("/")
def home():
    return render_template("home.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['User_name']
        session['user'] = user
        flash("Login successful")
        return redirect(url_for('user'))

    else:

        if "user" in session:
            return redirect(url_for("user"))
            flash("You are alredy in the page")
        return render_template('login.html')


@app.route('/user')
def user():
    if 'user' is session:
        user = session['user']
        return f"You logged in as {user}"
    else:
        return render_template("user.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("You have been logged out!", "info")
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(debug=True)
