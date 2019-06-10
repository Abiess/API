from Setup import db, ma



class Contact(db.Model):
    db.Column('Telefon', db.Integer)
    db.Column('Email', db.Integer)
    db.Column('CreationDate', db.datetime)
    User_id = db.Column(db.Integer, db.ForeignKey('user.id'))


def __init__(self, Telefon, Email, CreationDate,User_id ):
        self.Telefon = Telefon
        self.Email = Email
        self.CreationDate = CreationDate
        self.User_id = User_id

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('Telefon','Email')


user_schema = UserSchema()
users_schema = UserSchema(many=True)