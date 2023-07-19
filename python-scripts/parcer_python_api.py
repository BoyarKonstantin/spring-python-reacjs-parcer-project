from flask import Flask
from flask_restful import Resource, Api
from parcers import Parcers
from postgres_api import ParcerPostgresAPI

app = Flask("ParcerPythonAPI")
api = Api(app)
parcer = Parcers()
postgres_api_cursor = ParcerPostgresAPI()

class ParcerPythonAPI(Resource):

    def get(self):
        
        print(postgres_api_cursor.get_items())
        return postgres_api_cursor.get_items()
        
    def post(self, url):
        return parcer.ebayParcer("https://www.ebay.co.uk/b/Apple-Mobile-Smartphones/9355/bn_449685?LH_ItemCondition=1000%7C1500&rt=nc&_udlo=280&mag=1")

api.add_resource(ParcerPythonAPI, "/all")
if __name__ == "__main__":
    app.run()