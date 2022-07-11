from flask_mysqldb import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1', user='root', password='Gogoll90@', port=3306)
cursor = conn.cursor()


def ler_hotel(hotelid):
    cursor.execute(f'select * from API.APIHotel where hotelid = {hotelid}')
    dados = cursor.fetchall()
    if dados:
        Json = {
            "Hotelid": dados[0][0],
            "Hotelnome": dados[0][1],
            "Diaria": dados[0][2],
            "Estrelas": dados[0][3]
        }

        return Json

    else:
        return False


def registrar_hotel(nome,diaria,estrelas):
    cursor.execute(f'insert into API.APIHotel (hotelnome,diaria,estrelas)'
                   f' values ("{nome}",{diaria},{estrelas})')
    conn.commit()
    return True

def atualizar_hotel(hotelid,nome,diaria,estrelas):
    cursor.execute(f'UPDATE API.APIHotel SET hotelnome = "{nome}", diaria = {diaria}, estrelas = {estrelas} WHERE hotelid = {hotelid};')
    conn.commit()
    return True

def deletar_hotel(hotelid):
    cursor.execute(f'DELETE FROM API.APIHotel WHERE hotelid = {hotelid}')
    conn.commit()
    return True
