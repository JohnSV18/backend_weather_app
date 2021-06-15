import requests, json
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class PostResource(Resource):
    def get(self):
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        url = BASE_URL + "q=" + "san francisco" + "&appid=" + "4647aaef88d6e0fbf8feeb4ce0f0cb50"
        response = requests.get(url)
        
        # if response.status == 200:
        return {'data': response.json() }

    def post(self):
        return {'data': 'post request' }


api.add_resource(PostResource, '/weather')





if __name__ == '__main__':
    app.run(debug=True)