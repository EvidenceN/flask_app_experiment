from flask import Flask, render_template, request
import requests
from .database import DB, fav_cats

def test_app():
    # define and instantiate application
    app = Flask(__name__)

    # Setting up/configuring database
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"

    # stop tracking modifications on sqlalchemy config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # how the database knows about the app
    DB.init_app(app)

    # define home page
    @app.route('/', methods=['POST','GET'])
    def home():
        return render_template('home.html', title="first app!!", picture=images(), breeds = list_breed())

    # function to get random cat images
    def images():
        image = requests.get('https://api.thecatapi.com/v1/images/search')
        cats = image.json()[0]['url']
        return cats

    #list of cat breeds put in a dictionary
    def list_breed():
        breed_list = requests.get('https://api.thecatapi.com/v1/breeds')
        breeds = {}
        for breed_type in breed_list.json():
            breeds[breed_type['id']] = breed_type['name']

        return breeds

    # calling the API to search for cats by breed
    def search_cat(cat = ''):
        search = requests.get(f"https://api.thecatapi.com/v1/images/search?breed_ids={cat}")
        result = search.json()[0]['url']
        return result

    # a function to search for cats by breed
    # https://api.thecatapi.com/v1/images/search?breed_ids={cat}
    # https://api.thecatapi.com/v1/breeds/search?

    # page where submit(cats by category) button in home.html lands with the image of a new cat
    @app.route('/breed', methods=['POST'])
    def breed():
        cat = request.values['category'] # get the values from the dictionary in home.html
        image = search_cat(cat) # call the search cat function and pass in the id(values) as the parameter
        breeds = list_breed() # just call the list_breed function
        breed = breeds[cat] # call the id(key) from the list_breed() dictionary which returns the value associated with it as the name of  the cat displayed on the screen.
        return render_template('home.html', title="first app!!", picture=image, breeds = breeds, breed=breed)

    # stop tracking modifications on sqlalchemy config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return 'Database has been reset'

    # function for saving cat pictures into a database
    @app.route('/saved-cats', methods = ["POST"])
    def saved_cats():
        name_id = request.values['category'] #get the breed id of the cat
        breeds = list_breed() #dictionary with breed names
        name = breeds[name_id] # get the breed(value) of the cat from the name_id(key)
        link = request.values['CAT_URL'] #get the value from this name which is defined in home.html
        liked_cats = fav_cats(link=link, breed=name, breed_id=name_id)

        DB.session.add(liked_cats)

        DB.session.commit()

        return render_template('home.html', title="first app!!", picture=images(), breeds = list_breed())

    @app.route('/favorites')
    def favorites():
        faves = fav_cats.query.with_entites(fav_cats.link)
        return render_template("cat_faves.html", faves=faves, title='favorite cats')


    # a function to search for cats by category
    @app.route('/category')
    def category():
        pass

    # a function to search for cats by file type(gifs or images)
    @app.route('/type')
    def file_type():
        pass

    return app