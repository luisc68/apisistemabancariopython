##from crypt import methods
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL


from config import config

app = Flask(__name__)
conexion = MySQL(app)
##METODO GET
##GET TODAS LAS CUENTAS DEL SISTEMA
@app.route('/cuenta', methods=['GET'])
def listar_cuenta():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM cuenta"
        cursor.execute(sql)
        datos = cursor.fetchall()
        cuentas = []
        for fila in datos:
            cuenta = {'id': fila[0], 'numero_cuenta': fila[1], 'nombre_titular': fila[2], 'primer_apellido_titular': fila[3], 'segundo_apellido_titular': fila[4], 'balance': fila[5], 'estado': fila[6], 'moneda': fila[7]}
            cuentas.append(cuenta)
        return jsonify({'cuentas': cuentas, 'mensaje': "Cuentas listadas.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})

##GET NUMERO_CUENTA
@app.route('/cuenta/<codigo>', methods=['GET'])
def listar_numero_cuenta(codigo):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM cuenta WHERE numero_cuenta = '{0}'".format(codigo) 
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            cuenta = {'id': datos[0], 'numero_cuenta': datos[1], 'nombre_titular': datos[2], 'primer_apellido_titular': datos[3], 'segundo_apellido_titular': datos[4], 'balance': datos[5], 'estado': datos[6], 'moneda': datos[7]}
            return cuenta
        else:
            return jsonify({'mensaje': "Curso Encontrado"})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})

##METODO POST
@app.route('/cuenta', methods=['POST'])
def registrar_cuenta():
        try:
            cursor = conexion.connection.cursor()
            sql = """INSERT INTO cuenta (id, numero_cuenta, nombre_titular, primer_apellido_titular, segundo_apellido_titular, balance, estado, moneda) 
            VALUES ({0}, {1}, '{2}', '{3}', '{4}', {5}, {6}, '{7}')""".format(request.json['id'], 
                                                                      request.json['numero_cuenta'], request.json['nombre_titular'], request.json['primer_apellido_titular'], request.json['segundo_apellido_titular'], request.json['balance'], request.json['estado'], request.json['moneda'])
            cursor.execute(sql)
            conexion.connection.commit()
            return jsonify({'mensaje': "Cuenta registrada."})
        except Exception as ex:
            return jsonify({'mensaje': "Error"})


##UPDATE CUENTA
@app.route('/cuenta/<codigo>', methods=['PUT'])
def actualizar_cuenta(codigo):
        try:
            cursor = conexion.connection.cursor()
            sql = """UPDATE cuenta SET nombre_titular = '{0}', primer_apellido_titular = '{1}', segundo_apellido_titular = '{2}', balance = {3}, estado = {4} 
            WHERE id = '{5}'""".format(request.json['nombre_titular'], request.json['primer_apellido_titular'], request.json['segundo_apellido_titular'], request.json['balance'], request.json['estado'], codigo)
            cursor.execute(sql)
            conexion.connection.commit()  
            return jsonify({'mensaje': "Cuenta actualizada.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    




##DELETE CUENTA
@app.route('/cuenta/<codigo>', methods=['DELETE'])
def eliminar_cuenta(codigo):
        try:
            cursor = conexion.connection.cursor()
            sql = "DELETE FROM cuenta WHERE numero_cuenta = '{0}'".format(codigo)
            cursor.execute(sql)
            conexion.connection.commit()
            return jsonify({'mensaje': "Cuenta eliminada."})
        except Exception as ex:
            return jsonify({'mensaje': "Error"})


        



def pagina_no_encontrada(error):
    return "<h1>Página no encontrada</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()