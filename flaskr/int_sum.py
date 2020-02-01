from flaskr import app
from flask import request

@app.route('/sum')
def sum():
    return str(int(request.args.get('a')) + int(request.args.get('b')))
