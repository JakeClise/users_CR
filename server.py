from flask import Flask, render_template
from user import User
app = Flask(__name__)
app.secret_key = "this is secret"


@app.route('/')
def dashboard():
    return render_template('dash.html')

@app.route('/go-users')
def go_users():
    users = User.get_all()
    print(users)
    return render_template('users.html', users = users)


if __name__ == "__main__":
    app.run(debug=True)