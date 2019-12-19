"""Experimental code"""

from flask import Flask, render_template
import requests
from .database import DB


# define global variable
APP = Flask(__name__)

# Setting up/configuring database
APP.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"

# define home page
@APP.route('/')
def home():
    return render_template('home.html', title="first app!!")


if __name__ == "__main__":
    APP.run()