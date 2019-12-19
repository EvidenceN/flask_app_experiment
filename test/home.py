from flask import Flask, render_template
import requests
from .database import DB

def test_app():
    # define and instantiate application
    app = Flask(__name__)

    # Setting up/configuring database
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"

    # define home page
    @app.route('/')
    def home():
        return render_template('home.html', title="first app!!")

    return app