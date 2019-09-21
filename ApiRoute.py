from flask import request, jsonify, send_from_directory, render_template, abort, g, redirect, url_for, Flask
import os
from Setup import app, db
from psnstatistik import psnstatistik, psnstatistiks_schema, psnstatistik_schema
from user import User, users_schema, user_schema
from todo import Todo, todos_schema, todo_schema
import datetime
from werkzeug.utils import secure_filename
from flask_httpauth import HTTPBasicAuth


auth = HTTPBasicAuth()


# endpoint to create new user
@app.route("/user", methods=["POST"])
def add_user():
    username = request.json['username']
    password = request.json['password']
    userart = request.json['userart']
    beruf = request.json['beruf']
    creationDate = datetime.datetime.utcnow()
    if username is None or password is None:
        abort(400)  # missing arguments
    if User.query.filter_by(username=username).first() is not None:
        abort(400)  # existing user
    new_user = User(username, password, userart, beruf, creationDate)
    new_user.hash_password(password)

    db.session.add(new_user)
    db.session.commit()

    # return jsonify(new_user)
    return jsonify({'username': new_user.username}), \
           201, {'Location': url_for('get_user', id=new_user.id, _external=True)}


# endpoint to show all users
@app.route("/user", methods=["GET"])
@auth.login_required
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result.data)


@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username = username).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True


@app.route('/user/verify')
@auth.login_required
def get_resource():
    return jsonify({'data': 'Hello, %s!' % g.user.id})


# endpoint to get user detail by id
@app.route("/user/<id>", methods=["GET"])
def user_detail(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)


# endpoint to update user
@app.route("/user/<id>", methods=["PUT"])
def user_update(id):
    user = User.query.get(id)
    username = request.json['username']
    password = request.json['password']
    userart = request.json['userart']
    beruf = request.json['beruf']

    user.username = username
    user.password = password
    user.Beruf = beruf
    user.userart = userart
    db.session.commit()
    return user_schema.jsonify(user)


# endpoint to delete user
@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)


######################################


# Todo handle ...###########################################

# endpoint to create new Todo
@app.route("/todo", methods=["POST"])
def add_todo():
    userID = request.json['User_id']
    subject = request.json['Subject']
    description = request.json['Description']
    creationDate = datetime.datetime.utcnow()
    AssignedTo = request.json['AssignedTo']
    Attachement = upload_file()
    Username = request.json['Username']

    new_todo = Todo(userID, subject, description, creationDate, AssignedTo, Attachement)

    db.session.add(new_todo)
    db.session.commit()
    # upload_file()
    return jsonify(new_todo)


# endpoint to show all todos

@app.route("/todo", methods=["GET"])
def get_todo():
    all_todos = Todo.query.all()
    result = todos_schema.dump(all_todos)
    return jsonify(result.data)


def abdellah(str):
    return str


# endpoint to get todo detail by id

@app.route("/todo/<id>", methods=["GET"])
def todo_detail(id):
    todo = Todo.query.get(id)
    return todo_schema.jsonify(todo)


# endpoint to update todo
@app.route("/todo/<id>", methods=["PUT"])
def todo_update(id):
    todo = Todo.query.get(id)
    UserID = request.json['User_id']
    subject = request.json['Subject']
    description = request.json['Description']

    todo.User_id = UserID
    todo.Subject = subject
    todo.Description = description

    db.session.commit()
    return todo_schema.jsonify(todo)


# endpoint to delete todo
@app.route("/todo/<id>", methods=["DELETE"])
def todo_delete(id):
    todo = Todo.query.get(id)
    db.session.delete(todo)
    db.session.commit()

    return todo_schema.jsonify(todo)


##################################Upload send Files#########################

@app.route('/templates/path:path')
def send_html(path):
    return send_from_directory('static', path)


@app.route('/templates/test')
def send1_html():
    return render_template('test.html')


# @app.route('/upload', methods=['POST'])
def upload_file():
    print(request.files)
    # checking if the file is present or not.
    if 'file' not in request.files:
        return "No file found"
        # flash('No file found')
        # return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
        # flash('No selected file')
        # return redirect(request.url)
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOADED_FILES'], filename))

    # flash('file successfully saved')
    return "url should be getted"


##################################################################
################################ handle the psnstatistic##################################################
# endpoint to create new psnstatistic
@app.route("/psnstatistik", methods=["POST"])
def add_psnstatistik():
    firstname = request.json['firstname']
    secondname = request.json['secondname']
    payedForme = request.json['payedForme']
    payedForyassine = request.json['payedForyassine']
    bill = request.json['bill']
    codeprice = request.json['codePrice']
    dt = datetime.datetime.utcnow()

    new_psnstatistik = psnstatistik(firstname,
                                    secondname,
                                    payedForme,
                                    payedForyassine,
                                    bill,codeprice,dt)

    db.session.add(new_psnstatistik)
    db.session.commit()

    return psnstatistik_schema.jsonify(new_psnstatistik)


# endpoint to show all psnstatistics

@app.route("/psnstatistik", methods=["GET"])
#@auth.login_required
def get_psnstatistik():
    all_psnstatistiks = psnstatistik.query.all()
    result = psnstatistiks_schema.dump(all_psnstatistiks)
    return jsonify(result.data)


def abdellah(str):
    return str


# endpoint to get psnstatistic detail by id

@app.route("/psnstatistic/<id>", methods=["GET"])
def psnstatistik_detail(id):
    psnstatistic = psnstatistik.query.get(id)
    return psnstatistik_schema.jsonify(psnstatistic)


# endpoint to delete psnstatistic
@app.route("/psnstatistic/<id>", methods=["DELETE"])
def psnstatistic_delete(id):
    psnstatistic = psnstatistik.query.get(id)
    db.session.delete(psnstatistic)
    db.session.commit()

    return psnstatistik_schema.jsonify(psnstatistic)


##########################################################################################################
if __name__ == '__main__':
    db.create_all()
    db.session.commit()

    app.run(debug=True, port=32)
