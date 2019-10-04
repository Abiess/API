from Setup import db, ma
class Pateient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    User_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    firstname = db.Column(db.String)
    secondname = db.Column(db.String)
    weight = db.Column(db.Integer )
    gender = db.Column(db.String)
    illnes = db.Column(db.String)    
    birthday = db.Column(db.Date)
   


    def __init__(self, User_id,  firstname, secondname, weight , gender, illness, birthday):
        self.firstname = firstname
        self.secondname = secondname
        self.weight = weight
        self.gender = gender
        self.illness = illness
        self.birthday = birthday
	self.User_id = User_id
     


class PatientSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('User_id','firstname', 'secondname', 'weight', 'gender', 'illness', 'birthday')


patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)



