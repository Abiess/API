from Setup import db, ma


class psnstatistik(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String )
    secondname = db.Column(db.String)
    payedForme = db.Column(db.String)
    payedForyassine = db.Column(db.String)
    codePrice = db.Column(db.Integer)
    bill = db.Column(db.Integer)

    datetime = db.Column(db.DateTime)

    def __init__(self, firstname,
                 secondname, payedForme,
                 payedForyassine, bill, cprice,dt
                 ):
        self.firstname = firstname
        self.secondname = secondname
        self.payedForme = payedForme
        self.payedForyassine = payedForyassine
        self.bill = bill
        self.codePrice = cprice
        self.datetime = dt


class psnstatistikSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('firstname','secondname', 'payedForme',
                  'payedForyassine',
                  'bill', 'codePrice','datetime' )


psnstatistik_schema = psnstatistikSchema()
psnstatistiks_schema = psnstatistikSchema(many=True)
