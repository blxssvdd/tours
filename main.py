from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse

import db_actions
from db import create_db


app = Flask(__name__)
api = Api(app)


class Tour(Resource):
    def get(self, id=0):
        if not id:
            tours = db_actions.get_tours()
            return row_to_json(tours)

        tour = db_actions.get_tour(id)
        if tour:
            return row_to_json([tour])

        return "Відсутні подорожі"

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("country")
        parser.add_argument("price")
        params = parser.parse_args()
        id = db_actions.add_tour(**params)
        answer = jsonify(f"Подорож успішно додано під id {id}")
        answer.status_code = 200
        return answer

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("country")
        parser.add_argument("price")
        params = parser.parse_args()
        answer = db_actions.update_tour(id, **params)
        answer = jsonify(answer)
        answer.status_code = 200
        return answer

    def delete(self, id):
        answer = jsonify(db_actions.delete_tour(id))
        answer.status_code = 200
        return answer


def row_to_json(tours: list):
    tours_json = []

    for tour in tours:
        tours_json.append({
            "id": tour.id,
            "country": tour.country,
            "price": tour.price
        })

    tours_json = jsonify(tours_json)
    tours_json.status_code = 200

    return tours_json


api.add_resource(Tour, "/api/tours/", "/api/tours/<int:id>/")


if __name__ == "__main__":
    create_db()
    app.run(debug=True, port=3000)