from flask import Flask
from flask_restful import Api
from resourses.hoteis import hoteis,hotel

app = Flask(__name__)
api = Api(app)


api.add_resource(hoteis,'/hoteis')
api.add_resource(hotel,'/hotel')

if __name__ == '__main__':
    app.run(debug=True)