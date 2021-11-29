from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager 

#first instance of sqlalchemy and name of database file defined
dataBase = SQLAlchemy()
dbName = "database.dataBase"


#creation of flask application
def initialise_app():
    app = Flask(__name__)
    
    #for securing cookies and session data + creating database
    app.config['SECRET_KEY'] = 'birkbeckmsc'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{dbName}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #this supresses event system warning
    dataBase.init_app(app)


    #import blueprint objects from their respective files
    from .views import views 
    from .auth import auth
    
    #register blueprint with the flask application
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')
 
    #imports classes from models.py
    from .models import User

    #this function is called to check whether
    #it is neccesary to create a new database
    initialise_database(app)
    
    #redirects user to sign in page if they click on homepage
    signin_manager = LoginManager()
    signin_manager.login_view = 'auth.sign_in'
    signin_manager.init_app(app)
    #This is telling flask to load user if they already have an account
    @signin_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
     
#if there is currently no file path for a database document(database.dataBase)
#then a new database will be created   
def initialise_database(app):
    if not path.exists('webapp/' + dbName):
        dataBase.create_all(app=app)
        print('database made')