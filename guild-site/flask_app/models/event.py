from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, re
from flask_app.models import member

DATABASE = 'guild_site'

class Event:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.start_date = data['start_date']
        self.start_time = data['start_time']
        self.end_date = data['end_date']
        self.end_time = data['end_time']
        self.type = data['type']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.rsvps = []
        self.non_rsvps = []


    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM events;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        events = []
        for event in results: #! taking dicts from DB and making event objects
            events.append( cls(event) )
        return events
    
    @classmethod
    def get_all_with_rsvps(cls) -> list:
        query = "SELECT * FROM rsvps RIGHT JOIN events on rsvps.event_id = events.id LEFT JOIN non_rsvps on non_rsvps.event_id = events.id GROUP BY events.id;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)

        rsvps = []
        for rsvp in results: #! taking dicts from DB and making rsvp objects
            rsvps.append((rsvp))
        return rsvps
        #  book = cls(results[0])

        # for row_from_db in results:
        #     author_data = {
        #         'id' : row_from_db['authors.id'],
        #         'name' : row_from_db['name'],
        #         'created_at' : row_from_db['authors.created_at'],
        #         'updated_at' : row_from_db['authors.updated_at']
        #     }
        #     book.authors.append(author.Author(author_data))
        # return book

    @classmethod
    def get_all_non_rsvps(cls) -> list:
        query = "SELECT * FROM non_rsvps JOIN on rsvps.event_id = events.id;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        for non_rsvp in results: #! taking dicts from DB and making non_rsvp objects
            non_rsvps.append(non_rsvp)
        return non_rsvps

    @classmethod
    def save_rsvp(cls, data):
        query = "INSERT INTO rsvps(member_id, event_id) VALUES (%(member_id)s, %(event_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def save_non_rsvp(cls, data):
        query = "INSERT INTO non_rsvps(member_id, event_id) VALUES (%(member_id)s, %(event_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
