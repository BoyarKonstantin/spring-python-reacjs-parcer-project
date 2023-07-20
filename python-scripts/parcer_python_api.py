from flask import Flask, request
from flask_restful import Resource, Api
from parcers import Parcers
from postgres_api import ParcerPostgresAPI
from flask_cors import CORS

app = Flask("ParcerPythonAPI")
api = Api(app)
parcer = Parcers()
postgres_api_cursor = ParcerPostgresAPI()
CORS(app)

class ParcerPythonAPI(Resource):
    def get(self, url):
        items = postgres_api_cursor.get_items()
        print(items)
        return items

    def post(self):
        data = request.get_json()
        url = data.get('url')
        if url:
            result = parcer.ebayParcer(url)
            return result
        else:
            return {'error': 'URL is missing in the request body.'}, 400

api.add_resource(ParcerPythonAPI, "/main")

if __name__ == "__main__":
    app.run()

