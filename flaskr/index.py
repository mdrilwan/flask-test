from flaskr import app

@app.route('/')
def index():
    return "Rest interface to perform operations like sum, concat, subtract"

