from crypt import methods
from urllib import request
from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "vinod"
app.permanent_session_lifetime = timedelta(minutes=2)


@app.route("/")
def home():
    return render_template("home.html")


@app.route('/success/<name>')
def success(name):
    return 'Hello ;) %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permnate = True
        user = request.form['User_name']
        return redirect(url_for('success', name=user))

    else:

        if "user" in session:
            return redirect(url_for("user"))
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
