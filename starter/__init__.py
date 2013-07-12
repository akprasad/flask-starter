from flask import Flask

app = Flask(__name__)
app.config.from_object('config.development')


# Endpoints and blueprints
import views
