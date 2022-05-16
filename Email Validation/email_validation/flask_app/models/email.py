from flask_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class Email:
    # using a class variable to hold my database name
    db = 'email_schema'
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query= "SELECT * FROM emails;"
        results = connectToMySQL(cls.db).query_db(query)
        emails = []
        for row in results:
            emails.append(cls(row))
        return emails

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

#Don't quite understand this yet
    # @staticmethod
    # def is_valid(email):
    #     is_valid = True
    #     query = "SELECT * FROM emails WHERE email = %(email)s;"
    #     results = connectToMySQL('email_schema').query_db(query,email)
    #     if len(results) >= 1:
    #         flash("Email already taken.")
    #         is_valid=False
    #     if not EMAIL_REGEX.match(email['email']):
    #         flash("Invalid Email!")
    #         is_valid=False
    #     return is_valid