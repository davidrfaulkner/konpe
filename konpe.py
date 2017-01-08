from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import reqparse
from json import dumps
import logging
import sqlite3

#Import konpe config
import konpe.config
#Import resources
from konpe.resources import Tournament
from konpe.resources import ConfigRegion


konpe.config.SECRETAPIKEY = "NEWSECRET"
#logging.basicConfig(level=logging.DEBUG, filename='konpe_debug.log')

app = Flask(__name__)
api = Api(app)





api.add_resource(Tournament, '/Tournament')
api.add_resource(ConfigRegion, '/Config/Region')


if __name__ == '__main__':
     app.run()
