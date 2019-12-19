from flask import Flask, render_template
import requests
from .database import DB

def test_app():
    # define and instantiate application
    app = Flask(__name__)

    # Setting up/configuring database
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"

    # define home page
    @app.route('/', methods=['POST','GET'])
    def home():
        return render_template('home.html', title="first app!!", picture=images())

    # function to get random cat images
    def images():
        image = requests.get('https://api.thecatapi.com/v1/images/search')
        cats = image.json()[0]['url']
        # add something to be able to display the breed of the cat and it's id
        return cats
        # add a button to generate random images

    # a function to search for cats by breed
    @app.route('/breed')
    def breed():
        pass

    # a function to search for cats by category
    @app.route('/category')
    def category():
        pass

    # a function to search for cats by file type(gifs or images)
    @app.route('/type')
    def file_type():
        pass

    return app