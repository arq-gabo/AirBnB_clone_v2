#!/usr/bin/python3

"""
Module for start Flask web application
"""

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """Show Hello HBNB! in the index page"""
    return('Hello HBNB!')


@app.route('/hbnb')
def hbnb():
    """Show HBNB if the argument of parameter url is /hbnb"""
    return('HBNB')


@app.route('/c/<text>')
def cis(text):
    """Show the argument of url"""
    return('C {}'.format(text.replace('_', ' ')))


@app.route('/python/')
@app.route('/python/<text>')
def python(text="is cool"):
    """Show python Following the value of the text value"""
    return("Python {}".format(text.replace('_', ' ')))


@app.route('/number/<int:n>')
def number(n):
    """Show number the value of the number in the URL"""
    return("{} is a number".format(n))


@app.route('/number_template/<int:n>')
def htmlnumber(n):
    """Show the html page if "n" in URL is a integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def htmlnumber2(n):
    """Show the html page if "n" in URL is pair or even or odd """
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
