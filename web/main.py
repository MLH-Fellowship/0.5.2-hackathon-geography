from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
    # return render_template('index.html')

# @app.route('/test')
# def index2():
#     return 'Dicking around with Flask'

# @app.route('/<name>')
# def index3(name):
#     return 'Hello {}'.format(name)

# @app.route('/anything')
# def index4():
#     return redirect(url_for('index3', name='Kai'))