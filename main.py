#Web application design inspired by TechWithTim, I used his tutorial as guidance step by step when first developing
#my flask application
#https://www.youtube.com/watch?v=dam0GPOAvVI&ab_channel=TechWithTim
#https://github.com/techwithtim/Flask-Web-App-Tutorial


#For the pages and functionality in the levels and exercises pages, I did not follow any tutorials 
#but searched for various information on implementing select features

#this script below will run the flask application itself

#••••••import app class/function package from __init__.py and label an instance of the class/function
#then when the class/function(object) is called, the app will run ••••••
from webapp import initialise_app

app = initialise_app()

#this runs the app and 'debug=True' 
#allows the server to automatically look out for any changes and rerun itself
if __name__ == '__main__':
    app.run(debug=True)
