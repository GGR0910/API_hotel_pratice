import DAO
from flask_restful import reqparse, Resource
from flask_jwt_extended import create_access_token,jwt_required, get_jwt
from BLACKLIST import BLACKLIST

argumentos = reqparse.RequestParser()
argumentos.add_argument('user_id', default=0 ,help="No id provided")


class users(Resource):
    def get(self):
        dados = argumentos.parse_args()
        usuario = DAO.ler_user(user_id=dados['user_id'])
        if usuario:
            return usuario
        return {'message':'Usuario não encontrado'}

    @jwt_required()
    def delete(self):
        dados = argumentos.parse_args()
        if DAO.deletar_user(user_id=dados['user_id']):
            return {'Message': 'Deletado com sucesso'}

    def post(self):
        argumentos.add_argument('user_login', required=True, help="No login provided")
        argumentos.add_argument('user_pass', required=True, help="No passwword provided")
        dados = argumentos.parse_args()

        if DAO.ler_user(user_id=dados['user_id']):
            return {'message': 'usuario já existente'}
        if DAO.criar_user(user_login=dados['user_login'], user_pass=dados['user_pass']):
            return {'message': 'criado com sucesso'}, 200

class user_login(Resource):

    @classmethod
    def post(cls):
        argumentos.add_argument('user_login', required=True, help="No login provided")
        argumentos.add_argument('user_pass', required=True, help="No passwword provided")
        dados = argumentos.parse_args()
        valores=DAO.ler_login(user_login= dados['user_login'])
        if valores[0] == dados['user_login']:
            if valores[1] == dados['user_pass']:
                token_acess = create_access_token(identity= valores[0])

                return token_acess
            return {'Message': 'Senha não corresponde'}
        return {'Message': 'Usuario não encontrado'}


class user_logout(Resource):
    @jwt_required()
    def post(self):
        jwt_token = get_jwt()['jti']
        BLACKLIST.add(jwt_token)
        return {'message':'logout made.'}


