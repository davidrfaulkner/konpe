from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import reqparse
from sqlalchemy import create_engine
from json import dumps

#Create a engine for connecting to SQLite3.
#Assuming salaries.db is in your app root folder
e = create_engine('sqlite:///konpe.db')

app = Flask(__name__)
api = Api(app)

#GLOBAL API KEY
#TODO Do this differently, maybe use decorator, and store a hash here
SECRETAPIKEY = "SECRET"

#Constants
#TODO do something with this data (minutes)
TIMEKATA = 3
TIMEKUMITE = 4

class Tournament(Resource):
    def get(self):
        conn = e.connect()
        query = conn.execute("select * from tournaments")
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result

class Participant(Resource):
    def get(self):
        conn = e.connect()
        query = conn.execute("select * from tournaments")
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result

    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('first_name', type=str, help='Email address to create user')
            parser.add_argument('password', type=str, help='Password to create user')
            args = parser.parse_args()

            return {'Email': args['email'], 'Password': args['password']}

        except Exception as e:
            return {'error': str(e)}

class Division(Resource):
    def get(self):
        conn = e.connect()
        query = conn.execute("select * from tournaments")
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result

class DivisionParticipants(Resource):
    def get(self):
        conn = e.connect()
        query = conn.execute("select * from tournaments")
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result

class ConfigDojo(Resource):
    def get(self):
        conn = e.connect()
        query = conn.execute("select Value from Config where Key = 'Dojos'")
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result

class ConfigRegion(Resource):
    def get(self):
        conn = e.connect()
        query = conn.execute("select Value from Config where Key = 'Countries'")
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result

class ConfigCountry(Resource):
    def get(self):
        conn = e.connect()
        query = conn.execute("select Value from Config where Key = 'Regions'")
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result

class ConfigGrade(Resource):
    def get(self):
        conn = e.connect()
        query = conn.execute("select Value from Config where Key = 'Grades'")
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result

api.add_resource(Departmental_Salary, '/dept/<string:department_name>')
api.add_resource(Departments_Meta, '/departments')

if __name__ == '__main__':
     app.run()
