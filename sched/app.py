from flask import Flask

# Create a python object named app that is a WSGI application.
#   __name__ argument tells Flask to look in the current module (file) for resources
app = Flask(__name__)

# Set up function to handle requests to URL '/' (aka View functions)
#   View functions return strings when requests made
@app.route('/')
def hello():
    return 'Hello world!'

if __name__ == '__main__':
    pass
    # Run the python dev web server, but only if this file called directly (not via import)
    #app.run()
    # When run, should see: "Running on http://127.0.0.1:5000/"

    # If need app to be accessible on network, replace 'app.run()' with:
    #   app.run('0.0.0.0') or app.run('0.0.0.0', 8000) to listen on port 8000, etc...
    #app.run(debug=True)
    # Do not use debug mode on live server!

    # Alternatively, you can use Flask-Script with a manage.py file to manage
    #   how you want to run the app. This way you don't need to enter
    #   app.run() within this program file.
