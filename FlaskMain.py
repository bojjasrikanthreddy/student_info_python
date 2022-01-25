from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast


app = Flask(__name__)
api = Api(app)


class Users(Resource):
    # methods go here
    def get(self):
        data = pd.read_csv('users.csv')
        data = data.to_dict()
        return {'data': data}, 200
    pass


class Locations(Resource):
    # methods go here
    pass


api.add_resource(Users, '/users')  # '/users' is our entry point
api.add_resource(Locations, '/locations')  # and '/locations' is our entry point for Locations

if __name__ == '__main__':
    app.run()  # run our Flask app

