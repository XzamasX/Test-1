from flask import Flask,jsonify, request
import mysql.connector
            
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    port=3306,
    database='registro1',
)


app = Flask (__name__)

#@ definicion de decorador 
@app.route('/')
def index():
    return'Hola mundo'



@app.route('/contacto')
def contacto():
    return'en la pagina de contacto'

@app.post('/usuarios')
def crearUsuarios():
    datos = request.json
    cursor = db.cursor()
    cursor = db.execute('''INSERT INTO usuario(Nombre, Correo, Contraseña)
    VALUE(%s,%s,%s)''',(
        datos['Nombre'],
        datos['Correo'],
        datos['contraseña']
    ))
    db.commit()

    return jsonify({
        "mensajes": "usuario almacendo" 
    })

@app.get('/encuestas')
def obtenerEncuestas():
    return jsonify([
        {
            "Id":1,
            "name": "Encuesta de sastisfacion de clientes"
        },
        {
            "Id":2,
            "name": "Encuestas de satisfaccion de empleados"
        }
    ])

app.run(debug=True)
