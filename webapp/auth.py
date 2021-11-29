#The account pages templates are rendered in auth.py
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import dataBase
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

#LOGIN FUNCTIONALITY
@auth.route('/sign-in',methods=['GET', 'POST'])
def sign_in():
    #retrieve email and password from form
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        #login back-end
        user = User.query.filter_by(email=email).first()
        if user: #if email exists
            if check_password_hash(user.password, password): #check if password associated with email is the same as password typed in form
                flash('Sign-in successful!', category='success')
                login_user(user, remember=True) #flask will remember user so they do not have to log in everytime they close the browser, unless they delete their browser history
                return redirect(url_for('views.home'))                 #if so, flash successful message
            else: #if it does not, then flash this message
                flash('Password incorrect, please try again.', category='error')
        else: #if no such email exists then flash error message
            flash('No such email', category='error')
    return render_template("sign-in.html", user=current_user)

#LOGOUT FUNCTIONALITY
@auth.route('/logout')
@login_required #ensures logout only occurs if a user is logged in
def logout():
    logout_user()
    return redirect(url_for('auth.sign_in'))

#REGISTER ACCOUNT FUNCIONALITY
#using the HTTP protocols, GET and POST, data entered in the form
#by the user is processed here to be put in the database
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')


        #checks if email already exists during registration
        user = User.query.filter_by(email=email).first()
        if user:
            flash('This email has already been used.', category='error')
        #Error handling - messages shown to user if inputs are wrong
        elif len(email) == 0:
            flash('You must enter an email.', category='error')
        elif len(first_name) < 1:
            flash('First name must have at least one character.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 8:
            flash('Password must be a minimum of 8 characters.', category='error')
        else:
            newUser = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            dataBase.session.add(newUser)
            dataBase.session.commit()
            login_user(newUser, remember=True) #flask will automatically sign in user once account is created
            flash('Your account has been created!', category='success')
            flash('Click on one of the levels below to begin', category='success')
            return redirect(url_for('views.home'))
            
            
    return render_template("register.html", user=current_user)
