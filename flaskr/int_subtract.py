from flaskr import app
from flask import request

@app.route('/subtract')
def subtract():
    return str(int(request.args.get('a')) - int(request.args.get('b')))
