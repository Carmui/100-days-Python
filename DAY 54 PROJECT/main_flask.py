from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello'

@app_route('/papa')
def say_bye():
    return 'Papa'

if __name__=="__main__":
    app.run()