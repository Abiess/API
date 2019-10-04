from Setup import db, ma
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    User_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    Subject = db.Column(db.String)
    Description = db.Column(db.String)
    CreationTime = db.Column(db.DateTime )
    AssignedTo = db.Column(db.String)
    Attachement = db.Column(db.String)
    Username = db.Column(db.String)
    TodoStatus = db.Column(db.String)


    def __init__(self, User_id, Subject, Description,CreationTime , AssignedTo, Attachement, Username, TodoStatus):
        self.User_id = User_id
        self.Subject = Subject
        self.Description = Description
        self.CreationTime = CreationTime
        self.AssignedTo = AssignedTo
        self.Attachement = Attachement
        self.Username = Username
        self.TodoStatus = TodoStatus


class TodoSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('User_id', 'Subject', 'Description', 'AssignedTo', 'Attachement', 'Username', 'CreationTime', 'TodoStatus')


todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)
