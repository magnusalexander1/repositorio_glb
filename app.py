from flask import Flask, jsonify
import psycopg2


app = Flask(__name__)

@app.route('/empleados', methods=['GET'])
def obtener_empleados():
    # Conectar a la base de datos PostgreSQL
    conexion = psycopg2.connect(
        host="database-2.cbgaaim8e8l8.us-east-2.rds.amazonaws.com",
        database="database-2",
        user="postgres",
        password="i3:!kxx6z$1h.FU!ZADHxmB<w3+T"
    )

    # Consultar la vista de empleados
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM v_empleados_1")

    # Obtener los resultados de la consulta
    empleados = cursor.fetchall()

    # Cerrar la conexión a la base de datos
    cursor.close()
    conexion.close()
    # Convertir los resultados a formato JSON y devolverlos como respuesta
    response = empleados
    #response.headers['Content-Type'] = 'application/json'
    respuesta = {
        "respuesta": response
    }
    print("Respuesta: ", response)
    return respuesta

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)