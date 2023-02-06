from flask import Flask
import requests

app = Flask(__name__)


def make_bold(function):
    def fun_to_change():
        return "<b>" + function() + "</b>"
    return fun_to_change

def make_emphasis(function):
    def fun_to_change():
        return "<em>" + function() + "</em>"
    return fun_to_change

def make_underlined(function):
    def fun_to_change():
        return "<u>" + function() + "</u>"
    return fun_to_change

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello</h1>' \
           '<p>This is paragraph.</p>'

@app.route('/papa')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return 'Papa'

@app.route('/username/<name>/<int:number>')
def greet(name):
    return f'Hello now {name}, you are {number} years old!'


if __name__=="__main__":
    app.run(debug=True)