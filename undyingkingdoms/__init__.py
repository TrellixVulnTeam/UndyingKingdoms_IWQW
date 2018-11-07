import socket
import time

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_json import FlaskJSON
from flask_mail import Mail
import private_config

UPLOAD_FOLDER = 'undyingkingdoms/static/uploads/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config.from_object('private_config')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

if 'liveweb' in socket.gethostname():
    app.config['SQLALCHEMY_DATABASE_URI'] = private_config.SERVER_DATABASE_URI

db = SQLAlchemy(app)

csrf = CSRFProtect(app)
csrf.init_app(app)

json = FlaskJSON(app)

app.config.update(dict(
    DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME=private_config.MAIL_USERNAME,
    MAIL_PASSWORD=private_config.MAIL_PASSWORD,
    MAIL_DEFAULT_SENDER='This seems to do nothing'
))
mail = Mail(app)


@app.errorhandler(404)
def not_found(error):
    print("Error:", error)
    return render_template('404.html'), 404


from flask_login import LoginManager
from undyingkingdoms.models.users import User

import undyingkingdoms.routes.index.home
import undyingkingdoms.routes.index.login
import undyingkingdoms.routes.index.logout

import undyingkingdoms.routes.gameplay.overview
import undyingkingdoms.routes.gameplay.economy
import undyingkingdoms.routes.gameplay.infrastructure
import undyingkingdoms.routes.gameplay.military
import undyingkingdoms.routes.gameplay.kingdom
import undyingkingdoms.routes.gameplay.attack
import undyingkingdoms.routes.gameplay.attack_results


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

db.drop_all()
time.sleep(1)
db.create_all()
time.sleep(1)


@login_manager.user_loader
def load_user(this_id):
    return User.query.get(this_id)
