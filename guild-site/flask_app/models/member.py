from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, re
from pprint import pprint
from flask_app.models import event

DATABASE = 'guild_site'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class Member:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.phone_number = data['phone_number']
        self.password = data['password']
        self.permissions = data['permissions']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data:dict) -> int:
        query = "INSERT INTO members (first_name, last_name, email, phone_number, password, permissions) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(phone_number)s, %(password)s, %(permissions)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_by_email(cls,data:dict) -> object or bool:
        query = "SELECT * FROM members WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @staticmethod
    def validate_user(member:dict) -> bool:
        is_valid = True # ! we assume this is true
        print(member['permissions'])
        if not EMAIL_REGEX.match(member['email']): 
            flash("Invalid email address")
            is_valid = False
        if len(member['phone_number']) < 10:
            flash("Please enter a valid phone number")
            is_valid = False
        if len(member['phone_number']) > 14:
            flash("Please enter a valid phone number")
            is_valid = False
        if member['password'] != member['confirm-password']:
            flash("Passwords do not match")
            is_valid = False
        if member['registration_key'] != "ruh":
            flash('You do not have the proper registration key')
            is_valid = False
        return is_valid