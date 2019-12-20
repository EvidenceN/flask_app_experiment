"""Database Schema"""
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

# add something to the database so that somebody can click the button "favorite" and it will store that image url, id, and breed

class fav_cats(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    link = DB.Column(DB.String(150))
    breed = DB.Column(DB.String(50))
    breed_id = DB.Column(DB.String(10))

# create 4 tables so that there will be table for saving files from random image page, from breed page, from type page, and from category page. 