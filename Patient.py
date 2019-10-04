from Setup import db, ma
class Pateient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String)
    secondname = db.Column(db.String)
    weight = db.Column(db.Integer )
    gender = db.Column(db.String)
	illness	 = db.Column(db.String)    
    birthday = db.Column(db.Date)
   


    def __init__(self, firstname, secondname, weight , gender, illness, birthday):
        self.firstname = firstname
        self.secondname = secondname
        self.weight = weight
        self.gender = gender
        self.illness = illness
        self.birthday = birthday
     


class PatientSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('firstname', 'secondname', 'weight', 'gender', 'illness', 'birthday')


patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)



