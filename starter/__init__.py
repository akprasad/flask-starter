import importlib

from flask import Flask, Blueprint
from flask.ext.assets import Bundle, Environment
from flask.ext.security import Security, SQLAlchemyUserDatastore
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config.development')


# Assets
assets = Environment(app)


# Database
db = SQLAlchemy(app)


# Security
from starter.auth.models import User, Role
datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, datastore)


# Endpoints and blueprints
import views

blueprints = ['auth']
for bp in blueprints:
    m = importlib.import_module('starter.%s.views' % bp)
    for name in dir(m):
        item = getattr(m, name)
        if isinstance(item, Blueprint):
            app.register_blueprint(item)
