from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ksdgfiwuregfwileurgvbwelikjvbqio;eugfilweugblu'
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///maindb.db'
    db.init_app(app)

    from .sites import sites
    
    app.register_blueprint(sites, url_prefix='/')
    
    from .dbase import urldatabase

    with app.app_context():
        db.create_all()

    return app
    
