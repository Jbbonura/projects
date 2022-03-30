from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, re
from flask_app.models import member

DATABASE = 'guild_site'

class Event:
    pass