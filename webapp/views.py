#this is a blueprint of our application meaning it contains
#all the routes of the webapp
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

#All the routes to do with the view are defined here
@views.route('/')
@login_required #ensures that an account is needed to view homepage
def home():
    return render_template("home.html", user=current_user)

#All rendering of visuals for each question page for levels Entry level 3 and level 1
#are processed below. Also here is the logic where where correct and incorrect answers are processed.
@views.route('/home/E3/question1', methods=['GET', 'POST'])
def E3question1():
    if request.method == 'POST':
        answer = request.form.getlist('checkbox')
        if len(answer) == 1:
            if answer[0] == 'False':
                flash('Correct!', category='success')
                return redirect(url_for('views.E3question2'))
            else:
                flash('Incorrect!', category='error')
                return redirect(url_for('views.E3question2'))
        else:
            flash('Please only check one box.', category='error')
            
    return render_template("E3question1.html", user=current_user)

@views.route('/home/E3/question2', methods=['GET', 'POST'])
def E3question2():
    if request.method == 'POST':
        answer = request.form.getlist('checkbox')
        if len(answer) == 1:
            if answer[0] == 'True':
                flash('Correct!', category='success')
                return redirect(url_for('views.E3question3'))
            else:
                flash('Incorrect!', category='error')
                return redirect(url_for('views.E3question3'))
        else:
            flash('Please only check one box.', category='error')
            
    return render_template("E3question2.html", user=current_user)

@views.route('/home/E3/question3', methods=['GET', 'POST'])
def E3question3():
    if request.method == 'POST':
        answer = request.form.getlist('checkbox')
        if len(answer) == 1:
            if answer[0] == 'False':
                flash('Correct!', category='success')
                return redirect(url_for('views.E3question4'))
            else:
                flash('Incorrect!', category='error')
                return redirect(url_for('views.E3question4'))
        else:
            flash('Please only check one box.', category='error')
            
    return render_template("E3question3.html", user=current_user)

@views.route('/home/E3/question4', methods=['GET', 'POST'])
def E3question4():
    if request.method == 'POST':
        answer = request.form.getlist('checkbox')
        if len(answer) == 1:
            if answer[0] == 'True':
                flash('Correct!', category='success')
                return redirect(url_for('views.E3question5'))
            else:
                flash('Incorrect!', category='error')
                return redirect(url_for('views.E3question5'))
        else:
            flash('Please only check one box.', category='error')
            
    return render_template("E3question4.html", user=current_user)

@views.route('/home/E3/question5', methods=['GET', 'POST'])
def E3question5():
    if request.method == 'POST':
        answer = request.form.getlist('checkbox')
        if len(answer) == 1:
            if answer[0] == 'True':
                flash('Correct!', category='success')
                return redirect(url_for('views.E3question6'))
            else:
                flash('Incorrect!', category='error')
                return redirect(url_for('views.E3question6'))
        else:
            flash('Please only check one box.', category='error')
            
    return render_template("E3question5.html", user=current_user)

@views.route('/home/E3/question6', methods=['GET', 'POST'])
def E3question6():
    if request.method == 'POST':
        answer = request.form.getlist('checkbox')
        if len(answer) == 1:
            if answer[0] == 'False':
                flash('Correct!', category='success')
                return redirect(url_for('views.E3question7'))
            else:
                flash('Incorrect!', category='error')
                return redirect(url_for('views.E3question7'))
        else:
            flash('Please only check one box.', category='error')
            
    return render_template("E3question6.html", user=current_user)

@views.route('/home/E3/question7', methods=['GET', 'POST'])
def E3question7():
    if request.method == 'POST':
        answer = request.form.getlist('checkbox')
        if len(answer) == 1:
            if answer[0] == 'True':
                flash('Correct!', category='success')
                return redirect(url_for('views.E3question7'))
            else:
                flash('Incorrect!', category='error')
                return redirect(url_for('views.E3question7'))
        else:
            flash('Please only check one box.', category='error')
            
    return render_template("E3question7.html", user=current_user)

@views.route('/home/L1/question1', methods=['GET', 'POST'])
def L1question1():
    if request.method == 'POST':
        answer = request.form.getlist('checkbox')
        if len(answer) == 1:
            if answer[0] == 'c':
                flash('Correct!', category='success')
                return redirect(url_for('views.L1question2'))
            else:
                flash('Incorrect!', category='error')
                return redirect(url_for('views.L1question2'))
        else:
            flash('Please only check one box.', category='error')
            
    return render_template("L1question1.html", user=current_user)


@views.route('/home/L1/question2', methods=['GET', 'POST'])
def L1question2():
    if request.method == 'POST':
        answer = request.form.getlist('checkbox')
        if len(answer) == 1:
            if answer[0] == 'a':
                flash('Correct!', category='success')
                return redirect(url_for('views.L1question3'))
            else:
                flash('Incorrect!', category='error')
                return redirect(url_for('views.L1question3'))
        else:
            flash('Please only check one box.', category='error')
            
    return render_template("L1question2.html", user=current_user)


@views.route('/home/L1/question3', methods=['GET', 'POST'])
def L1question3():
    if request.method == 'POST':
        answer = request.form.getlist('checkbox')
        if len(answer) == 1:
            if answer[0] == 'd':
                flash('Correct!', category='success')
                return redirect(url_for('views.L1question4'))
            else:
                flash('Incorrect!', category='error')
                return redirect(url_for('views.L1question4'))
        else:
            flash('Please only check one box.', category='error')
            
    return render_template("L1question3.html", user=current_user)

@views.route('/home/L1/question4', methods=['GET', 'POST'])
def L1question4():
    if request.method == 'POST':
        answer = request.form.getlist('checkbox')
        if len(answer) == 1:
            if answer[0] == 'b':
                flash('Correct!', category='success')
                return redirect(url_for('views.L1question5'))
            else:
                flash('Incorrect!', category='error')
                return redirect(url_for('views.L1question5'))
        else:
            flash('Please only check one box.', category='error')
            
    return render_template("L1question4.html", user=current_user)

@views.route('/home/L1/question5', methods=['GET', 'POST'])
def L1question5():
    if request.method == 'POST':
        answer = request.form.getlist('checkbox')
        if len(answer) == 1:
            if answer[0] == 'c':
                flash('Correct!', category='success')
                return redirect(url_for('views.L1question6'))
            else:
                flash('Incorrect!', category='error')
                return redirect(url_for('views.L1question6'))
        else:
            flash('Please only check one box.', category='error')
            
    return render_template("L1question5.html", user=current_user)

@views.route('/home/L1/question6', methods=['GET', 'POST'])
def L1question6():
    if request.method == 'POST':
        answer = request.form.getlist('checkbox')
        if len(answer) == 1:
            if answer[0] == 'a':
                flash('Correct!', category='success')
                return redirect(url_for('views.L1question7'))
            else:
                flash('Incorrect!', category='error')
                return redirect(url_for('views.L1question7'))
        else:
            flash('Please only check one box.', category='error')
            
    return render_template("L1question6.html", user=current_user)

@views.route('/home/L1/question7', methods=['GET', 'POST'])
def L1question7():
    if request.method == 'POST':
        answer = request.form.getlist('checkbox')
        if len(answer) == 1:
            if answer[0] == 'd':
                flash('Correct!', category='success')
                return redirect(url_for('views.L1question7'))
            else:
                flash('Incorrect!', category='error')
                return redirect(url_for('views.L1question7'))
        else:
            flash('Please only check one box.', category='error')
            
    return render_template("L1question7.html", user=current_user)