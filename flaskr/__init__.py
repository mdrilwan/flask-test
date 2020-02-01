from flask import Flask

app = Flask(__name__)

from flaskr import index
from flaskr import int_sum
from flaskr import int_subtract
from flaskr import concat
