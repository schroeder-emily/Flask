from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db_name = 'belt_schema'

class Car:
    db_name = 'belt_schema'
    def __init__(self,db_data):
        self.id = db_data['id']
        self.price = db_data['price']
        self.model = db_data['model']
        self.make = db_data['make']
        self.year = db_data['year']
        self.description = db_data['description']
        self.user_id = db_data['user_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO cars (price, model, make, year, description, user_id) VALUES (%(price)s,%(model)s,%(make)s,%(year)s,%(description)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cars;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_cars = []
        for row in results:
            print(row['year'])
            all_cars.append( cls(row) )
        return all_cars
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM cars WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE cars SET year=%(year)s, model=%(model)s, make=%(make)s, year=%(year)s, description=%(description)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM cars WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod
    def validate_car(car):
        is_valid = True
        query = "SELECT * FROM cars WHERE description = %(description)s;"
        results = connectToMySQL(db_name).query_db(query,car)
        if len(car['price']) <= 0:
            is_valid = False
            flash("Price must be greater than 0","car")
        if len(car['year']) <= 0:
            is_valid = False
            flash("Year must be greater than 0","car")
        if car['model'] == "":
            is_valid = False
            flash("Please enter a model","car")
        if car['make'] == "":
            is_valid = False
            flash("Please enter a make","car")
        if car['description'] == "":
            is_valid = False
            flash("Please enter a description","car")
        return is_valid
