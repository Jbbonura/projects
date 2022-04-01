from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, re

DATABASE = 'guild_site'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Interested_User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.phone_number = data['phone_number']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data:dict) -> int:
        query = "INSERT INTO interested_users (first_name, last_name, email, phone_number) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(phone_number)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_user(interested_user:dict) -> bool:
        is_valid = True # ! we assume this is true
        if len(interested_user['first_name']) < 1:
            flash("Please enter a first name")
            is_valid = False
        if len(interested_user['last_name']) < 1:
            flash("Please enter a last name")
            is_valid = False
        if not EMAIL_REGEX.match(interested_user['email']): 
            flash("Invalid email address")
            is_valid = False
        if len(interested_user['phone_number']) < 10:
            flash("Please enter a valid phone number")
            is_valid = False
        if len(interested_user['phone_number']) > 14:
            flash("Please enter a valid phone number")
            is_valid = False
        return is_valid
