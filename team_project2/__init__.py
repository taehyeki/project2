from flask import Flask
from pymongo import MongoClient

client = MongoClient('localhost',27017)


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    from .views import main_views, auth1, file
    app.register_blueprint(main_views.bp)
    app.register_blueprint(auth1.bp)
    app.register_blueprint(file.bp)
    return app