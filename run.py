from datetime import datetime
import requests
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_mongoengine import MongoEngine
from config import Config
import datetime

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
db = MongoEngine()
db.init_app(app)


class WeatherMood(db.Document):
    """Class for the weather and mood with the data type that it's supposed to take"""
    # This is the data that we will be collecting into the database
    mood = db.StringField()
    date = db.DateTimeField()
    temperature = db.StringField()
    description = db.StringField()
    
    def __init__(self, mood, description, date, temperature, *args, **kargs):
        super(WeatherMood, self).__init__(*args, **kargs)
        
        self.date = date
        self.mood = mood
        self.temperature = temperature
        self.description = description
        


class PostResource(Resource):
    """Posting the mood and getting the weather data for the current day"""
    # This get method will get all the moods that have been collected by the database
    def get(self):
        moods = WeatherMood.objects()

        return jsonify(moods)
    
    def post(self):
        """Checks to see if there is a mood attribute in the file, if it does, then it will return all the data colected along with the mood"""
        test = request.get_json()
        
        if test['mood']:
            response = requests.get(Config.URL)
            date1 =  datetime.datetime.fromtimestamp(int(response.json()['dt']))
            print(date1)
            
            weather_mood = WeatherMood(mood=test['mood'],
                                       description=response.json()['weather'][0]['description'],
                                       date=date1,
                                       temperature=str(response.json()['main']['temp']))
            weather_mood.save()
        
        return jsonify(test)

class WeatherResource(Resource):
    """This class is in charge of returning all """
    def get(self):
        response = requests.get(Config.URL)
        print(response) 
        return {
            'result' : response.json()
        }
# Route that returns all data for the weather that day
api.add_resource(WeatherResource, '/weather')
# Route that then returns the mood a long with the weather information(POST) and get's added to the database
api.add_resource(PostResource, '/mood')


if __name__ == '__main__':
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)