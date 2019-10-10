from Setup import db, ma
class medicine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('Patient.id'))
    name = db.Column(db.String)
    deadline = db.Column(db.DateTime)
    consumption = db.Column(db.Integer )
    amount = db.Column(db.Integr)
    Kind = db.Column(db.String)    
    totalamount = db.Column(db.Integer)
   


    def __init__(self,patient_id, name, deadline, consumption , amount, kind, totalamount):
        self.name = name
        self.deadline = deadline
        self.consumption = consumption
        self.amount = amount
        self.kind = kind
        self.totalamount = totalamount
        self.patient_id = patient_id
     


class MedicineSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('patient_id','name', 'deadline', 'weight', 'consumption', 'amount', 'kind','totalamount')


medicine_schema = MedicineSchema()
medicines_schema = MedicineSchema(many=True)






