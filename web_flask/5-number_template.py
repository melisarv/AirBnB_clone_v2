#!/usr/bin/python3
''' script that starts a Flask web application '''
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    ''' Returns a text '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' Returns "HBNB" '''
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    ''' Returns a text starting with "C" '''
    return ("C " + text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    ''' Returns a text starting with "Python" '''
    return ("Python " + text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    ''' Display "<n> is a number" only if n is an integer '''
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    ''' Displays an HTML page if n is an integer '''
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run()
