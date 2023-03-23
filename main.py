import os

from flask import Flask, redirect, render_template, request, session, url_for
from helpers import get_users, hash_password

__winc_id__ = "8fd255f5fe5e40dcb1995184eaa26116"
__human_name__ = "authentication"

app = Flask(__name__)

app.secret_key = os.urandom(16)


@app.route("/home")
def redirect_index():
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("index.html", title="Index")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/lon")
def lon():
    return render_template("lon.html", title="League of Nations")

# https://realpython.com/introduction-to-flask-part-2-creating-a-login-page/


dict_users = get_users()


@app.route("/login", methods=["GET", "POST"])
def login():
    errorUsername = None
    errorPassword = None
    if request.method == "POST":
        for Username, Password in dict_users.items():
            username = request.form.get("username")
            password = request.form.get("password")
            hashed_password = hash_password(password)
            if Username == username:
                errorUsername = "The username was correct"
            else:
                errorUsername = "Wrong username"
                redirect(url_for('login', errorUsername=True))
                if hashed_password == Password:
                    return render_template("dashboard.html", title="dashboard")
                else:
                    if username in dict_users:
                        errorUsername = "username was correct"
                        errorPassword = "Pasword incorrect"
                        redirect(url_for('login', title="Login",
                                 errorUsername=True,  errorPassword=True))
                    if username not in dict_users:
                        errorPassword = "Pasword incorrect"
                        errorUsername = "username was NOT correct"
                        redirect(url_for('login', title="Login",
                                 errorUsername=True,  errorPassword=True))
    return render_template("login.html", title="Login", errorPassword=errorPassword, errorUsername=errorUsername)


@app.route("/dashboard")
def dashboard():
    # YOUR SOLUTION HERE
    pass


@app.route("/logout", methods=["GET", "POST"])
def logout():
    # YOUR SOLUTION HERE
    pass


if __name__ == '__main__':
    app.run(debug=True)
