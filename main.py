from flask import Flask
from flask_restful import Api
from resourses.hoteis import hotel
from resourses.usuario import users

app = Flask(__name__)
api = Api(app)

api.add_resource(users, '/usuarios')
api.add_resource(hotel, '/hotel')

if __name__ == '__main__':
    app.run(debug=True)
