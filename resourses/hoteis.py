from flask_restful import Resource, reqparse
import DAO

argumentos = reqparse.RequestParser()
argumentos.add_argument('hotelid', default=0)


class hotel(Resource):

    def addargsreq(self):
        argumentos.add_argument('hotelnome', required=True,help="Lack of name")
        argumentos.add_argument('diaria', required=True,help="Lack of daily price")
        argumentos.add_argument('estrelas', required=True,help="Lack of stars")
        return

    def get(self):
        dados = argumentos.parse_args()
        hotel = DAO.ler_hotel(hotelid=dados['hotelid'])
        if hotel:
            return hotel
        return {"Mensagem": "Hotel does not exist"}

    def post(self):
        self.addargsreq()
        dados = argumentos.parse_args()
        hotel = DAO.registrar_hotel(nome=dados['hotelnome'], diaria=dados['diaria'], estrelas=dados['estrelas'])
        if hotel:
            return {f"hotel {dados['hotelnome']}": "Salvo"}, 200
        return 400

    def put(self):
        dados = argumentos.parse_args()
        resposta = DAO.ler_hotel(hotelid=dados['hotelid'])
        if resposta:
            self.addargsreq()
            if DAO.atualizar_hotel(hotelid=dados['hotelid'], nome=dados['hotelnome'], diaria=dados['diaria'],
                                   estrelas=dados['estrelas']):
                return {f"Hotel {dados['hotelnome']}": "atualizado"}

        else:
            self.post()

            return {'Message:': "Hotel not found, created"}

    def delete(self):
        dados =argumentos.parse_args()
        if DAO.deletar_hotel(hotelid= dados['hotelid']):
            return {"Message" : "daleted with sucess"}, 200


