from Setup import db, ma


class psnstatistik(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String )
    secondname = db.Column(db.String)
    payedForme = db.Column(db.String)
    payedForyassine = db.Column(db.String)
    bill = db.Column(db.Integer)
    codePrice = db.Column(db.Integer)
    CreationDateTime = db.Column(db.DateTime)

    def __init__(self, firstname,
                 secondname, payedForme,
                 payedForyassine, bill,
                 codePrice, datetimecreation
                 ):
        self.firstname = firstname
        self.secondname = secondname
        self.payedForme = payedForme
        self.payedForyassine = payedForyassine
        self.bill = bill
        self.codePrice = codePrice,
        self.CreationDateTime = datetimecreation


class psnstatistikSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('firstname','secondname', 'payedForme',
                  'payedForyassine',
                  'bill', 'codePrice', 'datetimecreation' )


psnstatistik_schema = psnstatistikSchema()
psnstatistiks_schema = psnstatistikSchema(many=True)
