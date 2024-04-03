#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Plant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Plants(Resource):
    def get(self):
        response_dict_list = [p.to_dict() for p in Plant.query.all()]
        response = make_response(response_dict_list, 200)
        return response
api.add_resource(Plants, '/plants')

class PlantByID(Resource):
    pass
        

if __name__ == '__main__':
    app.run(port=5555, debug=True)
