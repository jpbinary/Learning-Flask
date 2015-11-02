'''
    Explore how Flask works
'''

from flask import Flask, make_response
from flask import request

app = Flask(__name__)

#----------------------------------------------------------------------------------------------------------------------#
# dump request data to the console for debugging

def dump_request_detail(request):
    request_detail = """
# Before request
request.endpoint: {request.endpoint}
request.method: {request.method}
request.view_args: {request.view_args}
request.args: {request.args}
request.form: {request.form}
request.user_agent: {request.user_agent}
request.files: {request.files}
request.is_xhr: {request.is_xhr}

## request.headers ##
{request.headers}
    """.format(request=request).strip()
    return request_detail

@app.before_request
def callme_before_every_request():
    # Demo only: the before_request hook.
    app.logger.debug(dump_request_detail(request))

@app.after_request
def callme_after_every_response(response):
    # Demo only: the after_request hook.
    app.logger.debug('# After Request #\n' + repr(response))
    return response

#----------------------------------------------------------------------------------------------------------------------#

@app.route('/string/')
def return_string():
    return 'Hello, world. (string)'

@app.route('/object/')
def return_object():
    headers = {'Content-Type': 'text/plain'}
    return make_response('Hello, world. (object)', 200, headers)

@app.route('/tuple/')
def return_tuple():
    return 'Hello, world. (tuple)', 200, {'Content-Type': 'text/plain'}


#----------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    app.run(debug=True)
