import os

from flask import Flask

from . import db

#Define my application/ Initilaized my application

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    db.init_app(app)
    app.config.from_mapping(
        SECRETE_KEY= 'foundations', #choose your secrete key
        DATABASE=os.path.join(app.instance_path, 'blog.sqlite'), #choose your database
    )
    
    
    #Use test-config if we have test, otherwise use config.py by default.
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)    
        
    #catching errors from running our root app
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass        
    
    
    
    #creating a route to our homepage
    @app.route('/home') # call this what you want
    def home(): #call this whatever you want
        return 'Welcome to our foundations blog page'
    
    return app