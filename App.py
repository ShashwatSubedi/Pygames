import csv
from flask import Flask, render_template, request

app = Flask(__name__)


users_file='userinfos.csv'

@app.route("/")
def home():
    return render_template("base.html", title="Welcome to My Website", message="Hello, User!", message2="Please Login to Proceed")

@ app.route("/login", methods=['GET','POST'])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # Add logic to authenticate user
        return f"Welcome, {username}!"
    return render_template("Login page.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            return "Passwords do not match!"
        return f"Welcome, {username}! You have successfully signed up."

    return render_template("Sign-up.html")

def save_in_csv(username, email, password):
    with open(users_file, mode='a', newline='') as file:
        add=csv.writer(file)
        add.writerow([username, email, password])

def initialize_csv():
    try:
        with open(users_file, mode='x', newline='') as file:
            add=csv.writer(file)
            add.writerow(['Username', 'Email', 'Password'])
    except FileExistsError:
        pass


if __name__ == "__main__":
    app.run(debug=False)
# @app.route('/<name>')
# def user(name):
#     return f'Hello {name}!'

# @app.route('/admin/')
# def admin():
#     return redirect(url_for('user', name='Admin!!!'))
if __name__=='__main__':
    initialize_csv()
    app.run(port=5001)
