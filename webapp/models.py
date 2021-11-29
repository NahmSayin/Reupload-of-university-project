#database models for storing user information and other data

#importing of relevant libraries and objects
from . import dataBase
from flask_login import UserMixin

#a class used to create a user object when a user submits their data
#this provides the guidelines of how the data will be stored in a uniform manner 
#we have here a unique id associated with the user, also their first name, email
#and password

class User(dataBase.Model, UserMixin):
    id = dataBase.Column(dataBase.Integer, primary_key=True)
    email = dataBase.Column(dataBase.String(200), unique=True)
    password = dataBase.Column(dataBase.String(200))
    first_name = dataBase.Column(dataBase.String(200)) 