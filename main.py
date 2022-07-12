from flask import Flask, jsonify
from flask_restful import Api
from resourses.hoteis import hotel
from resourses.usuario import users, user_login, user_logout
from flask_jwt_extended import JWTManager
from BLACKLIST import BLACKLIST

app = Flask(__name__)
api = Api(app)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = "Fuck"
app.config['JWT_BLACKLIST_ENABLED'] = True


@jwt.token_in_blocklist_loader(callback=callable)
def verificar_blacklist(token):
    return token['jti'] in BLACKLIST


@jwt.revoked_token_loader(callback=callable)
def revogar_token():
    return jsonify({"message": "You have been desloged"})


api.add_resource(users, '/usuarios')
api.add_resource(hotel, '/hotel')
api.add_resource(user_login, '/login')
api.add_resource(user_logout, '/logout')

if __name__ == '__main__':
    app.run(debug=True)
