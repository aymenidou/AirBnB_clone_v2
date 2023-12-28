#!/usr/bin/python3
'module for task 0'
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    'simple hello return'
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello():
    'simple hello return'
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_isfun(text):
    'return text argument'
    arg = text.replace('_', ' ')
    return 'C {}'.format(arg)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    'return text argument'
    arg = text.replace('_', ' ')
    return 'Python {}'.format(arg)


@app.route('/number/<int:n>', strict_slashes=False)
def check_number(n):
    'check if n is a Number'
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    'check if n is a Number'
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    'check if n is a Number'
    return render_template('6-number_odd_or_even.html', n=n, props='even' if (n % 2 == 0) else "odd")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
