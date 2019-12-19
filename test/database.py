"""Database Schema"""
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

# add something to the database so that somebody can click the button "favorite" and it will store that image url, id, and breed

# create 4 tables so that there will be table for saving files from random image page, from breed page, from type page, and from category page. 