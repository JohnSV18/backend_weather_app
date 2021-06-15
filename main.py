from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class PostResource(Resource):
    def get(self):
        return {'data': 'Get request' }

    def post(self):
        return {'data': 'post request' }


api.add_resource(PostResource, '/')
api.add_resource(PostResource, '/weather/int:id')




if __name__ == '__main__':
    app.run(debug=True)