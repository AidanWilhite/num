
import os
from flask import Flask, session

from maps.Guess import Guess
from maps.SetNum import Set


def create_app():
    app = Flask(__name__)
    #app.config['SECRET_KEY'] = 'gbyaeduhbifewh9upgh8u9ier9phgqh9iu8erghi809'
    app.config['SECRET_KEY'] = 'the random string'
    app.template_folder = os.path.abspath('frontend')
    # print(app.template_folder)
    app.register_blueprint(Guess)
    app.register_blueprint(Set)

    return app
