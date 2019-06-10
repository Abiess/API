from Setup import db, ma
import enum

class UserArt(enum.Enum):
    simpleUser = 'simpleUser'
    Handwerker = 'Handwerker'
    kunde = 'kunde'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120), unique=True)
    userart = db.Column(db.String)
    beruf = db.Column(db.String)
    creationTime = db.Column(db.DateTime)

    def __init__(self, username,  password, userart, beruf, creationTime):
        self.username = username
        self.password = password
        self.userart = userart
        self.beruf = beruf
        self.creationTime = creationTime

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('username','password', 'userart', 'beruf')


user_schema = UserSchema()
users_schema = UserSchema(many=True)