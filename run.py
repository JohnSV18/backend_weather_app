import requests, json
from flask import Flask
from config import Config
from flask_restful import Api, Resource

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

class PostResource(Resource):
    def get(self):
        response = requests.get(Config.URL)
    
        return {'data': response.json() }

    def post(self):
        return {'data': 'post request' }

api.add_resource(PostResource, '/weather')

if __name__ == '__main__':
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)