from flask import Flask, jsonify, request
import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password ='12345678',
    database = 'registro',
    port =3306
    
)

app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello world'



@app.post('/registro')
def crearpersonal_data():
    #request  => envia el cliente
    #response => lo que le voy a responder
    datos = request.json
    
    print(datos)

    cursor = db.cursor()

    cursor.execute('''INSERT INTO usuario(Nombre, Correo, Contraseña)
        VALUE(%s, %s, %s)''', (
        datos['Nombre'],
        datos['Correo'],
        datos['Contraseña'],
    ))

    db.commit()
    
    return jsonify({

        "mensaje": "usuario alamcenado correctamente"
    })


@app.get('/registro')
def listaUsuarios():
    cursor = db.cursor(dictionary=True)

    cursor.execute('select * from usuario')

    registros = cursor.fetchall()

    return jsonify(registros)




@app.put('/registro/<id>')
def actualizarUsuario(id):

    datos=request.json

    cursor = db.cursor()


    cursor.execute('''UPDATE usuario set Nombre=%s, 
        Correo=%s, Contraseña=%s where id=%s''',(
            datos['Nombre'],
            datos['Correo'],
            datos['Contraseña'],
            id
        ))
    
    db.commit()

    return jsonify({

        "mensaje": "usuario alamcenado correctamente"
    })  
    
    
@app.delete('/registro/<id>')
def eliminarUsuario(id):


    cursor = db.cursor()
    cursor.execute('DELETE FROM usuario where id=%s',(id,))


    db.commit()

    return jsonify({

        "mensaje": "usuario eliminado correctamente"
    })

@app.get('/registro/<id>')
def unUsuario(id):
    cursor = db.cursor()
    cursor.execute('DELETE FROM usuario where id=%s',(id,))


    db.commit()

    return jsonify({

        "mensaje": "usuario eliminado correctamente"
    })
    
app.run(debug=True)