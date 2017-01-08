from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import reqparse
from json import dumps
import logging
import sqlite3
#TODO tidy up imports later

#connecting to SQLite3.
sql = sqlite3.connect('konpe.db')
sql.row_factory = sqlite3.Row
#Turn off transactions for increased performance, commit() not required
sql.isolation_level = None

class Tournament(Resource):
    def get(self):
        cur = sql.execute("select * from tournaments")
        rows = cur.fetchall()
        cols = rows[0].keys()
        result = {'data': [dict(zip(tuple (cols) ,i)) for i in rows]}
        return result

    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('TournamentName', type=str)
            parser.add_argument('TournamentDate', type=str)
            parser.add_argument('TournamentLocation', type=str)
            parser.add_argument('TournamentRings', type=int)
            args = parser.parse_args()

            cur = sql.execute\
                ('INSERT INTO Tournaments (TournamentName, TournamentDate, TournamentLocation, TournamentRings) VALUES'
                 '(:TournamentName, :TournamentDate, :TournamentLocation, :TournamentRings);',
                 args)
            logging.debug(cur.lastrowid)
            return {'TournamentID': cur.lastrowid}
        except Exception as e:
            return {'error': str(e)}, 500

    def put(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('TournamentID', type=str, required=True)
            parser.add_argument('TournamentName', type=str)
            parser.add_argument('TournamentDate', type=str)
            parser.add_argument('TournamentLocation', type=str)
            parser.add_argument('TournamentRings', type=int)
            args = parser.parse_args()

            cur = sql.execute\
                ('UPDATE Tournaments SET TournamentName=:TournamentName, TournamentDate=:TournamentDate,'
                 'TournamentLocation=:TournamentLocation, TournamentRings=:TournamentRings '
                 'WHERE TournamentID = :TournamentID;',
                 args)
            return {'TournamentID': args['TournamentID']}
        except Exception as e:
            return {'error': str(e)}, 500

    def delete(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('TournamentID', type=int)
            args = parser.parse_args()
            cur = sql.execute\
                ('DELETE FROM Tournaments WHERE TournamentID = :TournamentID;',
                 args)
            return {'TournamentID': args['TournamentID']}
        except Exception as e:
            return {'error': str(e)}, 500

class Participant(Resource):
    def get(self):
        cur = sql.execute("select * from tournaments")
        rows = cur.fetchall()
        cols = rows[0].keys()
        result = {'data': [dict(zip(tuple (cols) ,i)) for i in rows]}
        return result

    def post(self):
        pass

class Division(Resource):
    def get(self):
        cur = sql.execute("select * from tournaments")
        rows = cur.fetchall()
        cols = rows[0].keys()
        result = {'data': [dict(zip(tuple (cols) ,i)) for i in rows]}
        return result

class DivisionParticipants(Resource):
    def get(self):
        cur = sql.execute("select * from tournaments")
        rows = cur.fetchall()
        cols = rows[0].keys()
        result = {'data': [dict(zip(tuple (cols) ,i)) for i in rows]}
        return result

class ConfigDojo(Resource):
    def get(self):
        cur = sql.execute("select Value from Config where Key = 'Dojos'")
        result = {'data': cur.fetchone()['Value']}
        return result

class ConfigRegion(Resource):
    def get(self):
        cur = sql.execute("select Value from Config where Key = 'Regions'")
        result = {'data': cur.fetchone()['Value']}
        return result

class ConfigCountry(Resource):
    def get(self):
        cur = sql.execute("select Value from Config where Key = 'Countries'")
        result = {'data': cur.fetchone()['Value']}
        return result

class ConfigGrade(Resource):
    def get(self):
        cur = sql.execute("select Value from Config where Key = 'Grades'")
        result = {'data': cur.fetchone()['Value']}
        return result
