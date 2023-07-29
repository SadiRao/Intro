from flask import Flask
from flask_mail import Mail, Message
from .home import homes
from .about import abouts
from .database import db
from .contact import contacts
from .gallery import galleries


app = Flask(__name__, template_folder='../templates', static_folder='../static')
mail = Mail(app)

def create_app():
    app.config['SECRET_KEY'] = 'hello'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///web.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = 'sadianadeem699@gmail.com'
    app.config['MAIL_PASSWORD'] = 'NSadia@2001'
    db.init_app(app)
    app.register_blueprint(homes)
    app.register_blueprint(abouts)
    app.register_blueprint(contacts)
    app.register_blueprint(galleries)
    
    with app.app_context():
        db.create_all()
    
    return app