a good practice is to run python web environments in a virtual environment.

#install virtual environment
pip install virtualenv

#folder structure should be as follows:
mysite
    Demo
        static
        templates
        

#this tells python where to create a virtual environment
#it creates a virtual folder named "virtual" in the web folder structure
python -m venv virtual

#now point the virtual python environment to install flask
C:\GitHub\Python_Scripts\mysite\virtual\Scripts
pip install flask

#finally run web as as new virtual python environment
python "C:\GitHub\Python_Scripts\mysite\Demo\script1.py"

#create account at heroku.com
#install heroku toolbelt
#during install make sure to say yes to add to PATH

#open cmd as admin and navigate to the Demo folder
cd C:\GitHub\Python_Scripts\mysite\Demo
heroku login 
#follow password prompts

#create new web app
heroku create data-web-test

#list all heroku webapps
heroku apps

#create 3 files in the demo folder
cd C:\GitHub\Python_Scripts\mysite\virtual\Scripts
pip freeze

#heroku server needsd this php library to run the python application
pip install gunicorn

#pip freeze again and check for gunicorn
#send that to a text file to tell heroku what to install
pip freeze > requirements.txt

#add Procfile to project

#add runtime.txt file to project

#create git repository
cd .\Demo\
git init

#add files to repository
# the "dot" means the current directory
git add .

#commit the changes
git commit -m "first commit"

#now tell heroku which app you are working on
heroku git:remote --app data-web-test

#now push changes to heroku
git push heroku master




