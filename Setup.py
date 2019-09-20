from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
import os
app = Flask(__name__,  static_url_path='/static')
app.secret_key = os.urandom(24)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'HM.sqlite')
app.config['UPLOADED_FILES'] = 'static/files'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

