'''
    Explore how Flask works
'''

from flask import Flask, make_response


app = Flask(__name__)

@app.route('/string/')
def return_string():
    return 'Hello, world. (string)'

@app.route('/object/')
def return_object:
    headers = {'Content-Type': 'text/plain'}
    return make_response('Hello, world. (object)', status=200, headers=headers)

