# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask
from flask_basicauth import BasicAuth


# Load Auth
panel_config_file = open("panel.config","r")
panel_config = json.loads(panel_config_file.read())
panel_config_file.close()

app = Flask(__name__, static_url_path='')


# Basic-Auth
app.config['BASIC_AUTH_USERNAME'] = panel_config['username']
app.config['BASIC_AUTH_PASSWORD'] = panel_config['password']
app.config['BASIC_AUTH_FORCE'] = True

basic_auth = BasicAuth(app)
# Database
#

#Constant

from . import config
app.logger.info('>>> {}'.format(app.config['MODE']))




from App.api import api_rest, api_bp
from App.client import client_bp


# Flask-Blueprint
app.register_blueprint(api_bp)
app.register_blueprint(client_bp)
