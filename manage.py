# Manage application with Flask-Script
#   which gives you the runserver and shell commands from the command line
from flask.ext.script import Manager
from sched.app import app

manager = Manager(app)
app.config['DEBUG'] = True # To turn on debugging

if __name__ == '__main__':
    manager.run()

# run app from the command line:
#   $ python manage.py runserver
#   $ python manage.py runserver -h 0.0.0.0 -p 8000