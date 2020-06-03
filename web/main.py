from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/test')
def index2():
    return 'Dicking around with Flask'

@app.route('/<name>')
def index3(name):
    return 'Hello {}'.format(name)