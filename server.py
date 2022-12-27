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

@app.route('/view/<int:id>')
def get_one_user(id):
    data = {
        "id":id
    }
    return render_template('one_user.html',user=User.get_one_user(data))

@app.route('/edit/<int:id>')
def go_edit_user(id):
    data = {
        "id":id
    }
    return render_template('edit_user.html',user=User.get_one_user(data))

@app.route('/edit-one-user', methods=["POST"])
def update_user():
    User.update(request.form)
    return redirect('/go-users')

@app.route('/delete/<int:id>')
def delete_user(id):
    users = User.get_all()
    data = {
        "id":id
    }
    return render_template('users.html', user=User.drop_user(data), users=users)





if __name__ == "__main__":
    app.run(debug=True)