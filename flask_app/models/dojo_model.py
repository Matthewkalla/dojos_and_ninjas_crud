from flask_app.config.mysqlconnection import connectToMySQL 
from flask_app import DATABASE
from flask_app.models import ninja_model

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


#the method to get all the dojos
    @classmethod
    def get_all(cls):
        query = """
        SELECT *
        FROM dojos
        """
        results = connectToMySQL(DATABASE).query_db(query)
        all_dojos = []
        for one_dojo in results:
            all_dojos.append( cls(one_dojo) )
        return all_dojos

#this method will create a new dojo
    @classmethod
    def create(cls, data): #give this method data
        #to insert the info we got from the user
        query="""
        INSERT INTO dojos (name)
        VALUES (%(name)s)
        """
        return connectToMySQL(DATABASE).query_db(query,data)

#this method will get one dojo
    @classmethod
    def get_one(cls, data):
        query = """
        SELECT *
        FROM dojos
        LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
        WHERE dojos.id = %(id)s
        """

        results = connectToMySQL(DATABASE).query_db(query,data)
        print(results)
        if results:
            dojo_instance = cls(results[0])
            ninjas_list = []

            for one_row in results: #hove
                #to provide a case where no dojos are found
                if one_row['ninjas.id'] == None:
                    return dojo_instance
                ninja_data = {
                    'id': one_row['ninjas.id'],
                    'created_at': one_row['ninjas.created_at'],
                    'updated_at': one_row['ninjas.updated_at'],
                    **one_row
                }
                print(ninja_data)
                ninja_instance = ninja_model.Ninja(ninja_data)
                ninjas_list.append(ninja_instance)

            dojo_instance.ninjas = ninjas_list
            return dojo_instance
        return False