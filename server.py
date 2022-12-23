from flask import Flask, render_template, redirect, request
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

@app.route('/go-create')
def go_create():
    return render_template('create_user.html')

@app.route('/create-user', methods=["POST"])
def create_user():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'], 
        "email": request.form['email']
    }
    User.save(data)
    return redirect('/go-users')


if __name__ == "__main__":
    app.run(debug=True)