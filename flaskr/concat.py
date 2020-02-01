from flaskr import app
from flask import request

@app.route('/concat')
def concat():
    return request.args.get('a') + request.args.get('b')
