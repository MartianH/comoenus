from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt


app = Flask(__name__)
app.config.from_object('comoenus.dev_config')
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
db = SQLAlchemy(app)
flask_bcrypt = Bcrypt(app)
rest_api = Blueprint('rest_api', __name__, url_prefix='/api')


import model
import views
import api
import errors
app.register_blueprint(rest_api)