from Setup import db, ma


class psnstatistik(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(120), unique=True)
    secondname = db.Column(db.String(120), unique=True)
    payedForme = db.Column(db.Boolean)
    payedForyassine = db.Column(db.Boolean)
    creationTime = db.Column(db.DateTime)
    bill = db.Column(db.Integer)
    codePrice = db.Column(db.Integer)

    def __init__(self, username,  password, userart, beruf, creationTime):
        self.username = username
        self.password = password
        self.userart = userart
        self.beruf = beruf
        self.creationTime = creationTime

class psnstatistikSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('firstname','secondname', 'payedForme', 'payedForyassine','bill', 'codePrice' )


psnstatistik_schema = psnstatistikSchema()
psnstatistiks_schema = psnstatistikSchema(many=True)
