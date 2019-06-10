from flask import request, jsonify, send_from_directory, render_template, flash, redirect, url_for
import os
from Setup import  app, db
from user import User, users_schema, user_schema
from todo import Todo, todos_schema,todo_schema
import  datetime
from werkzeug.utils import secure_filename


# endpoint to create new user
@app.route("/user", methods=["POST"])
def add_user():
    username = request.json['username']
    password = request.json['password']
    userart = request.json['userart']
    beruf = request.json['beruf']
    creationDate = datetime.datetime.utcnow()

    new_user = User(username,password, userart, beruf, creationDate)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user)


# endpoint to show all users
@app.route("/user", methods=["GET"])
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result.data)


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

    new_todo = Todo(userID, subject, description, creationDate, AssignedTo, Attachement)

    db.session.add(new_todo)
    db.session.commit()
    #upload_file()
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

#@app.route('/upload', methods=['POST'])
def upload_file():
    print (request.files)
    # checking if the file is present or not.
    if 'file' not in request.files:
        return "No file found"
        #flash('No file found')
        #return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
        #flash('No selected file')
        #return redirect(request.url)
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOADED_FILES'],  filename))

    #flash('file successfully saved')
    return "url should be getted"

##################################################################

if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    app.run(debug=True ,port = 32)

