from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app= Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'challenge'

conexion= MySQL(app)

@app.route('/')
def index():
        return "CHALLENGE - ARIDO SOFTWARE"

@app.route('/challenge')
def tables():
        try:
                cursor=conexion.connection.cursor()
                sql="SELECT name_alias, pass, create_time, status FROM us_sec"
                cursor.execute(sql)
                datos=cursor.fetchall()
                users=[]
                for fila in datos:
                        user={'name_alias':fila[0],'pass':fila[1],'create_time':fila[2],'status':fila[3]}
                        users.append(user)
                return jsonify({'users':users,'resultado':"Usuarios."})
        except Exception as ex:
            return "Error"

@app.route('/challenge/<name_alias>',methods=['GET'])
def alias(name_alias):
        try:
                cursor=conexion.connection.cursor()
                sql="SELECT name_alias, pass, create_time, status FROM us_sec WHERE name_alias = '{0}'".format(name_alias)
                cursor.execute(sql)
                data=cursor.fetchone()
                if data != None:
                        user={'name_alias':data[0],'pass':data[1],'create_time':data[2],'status':data[3]}
                        return jsonify({'users':user,'resultado':"Usuario encontrado."})
                else:
                        return jsonify({'resultado':"Usuario no encontrado."})
        except Exception as ex:
                return "Error"


@app.route('/challenge/GR')
def table():
        try:
                cursor=conexion.connection.cursor()
                sql1="SELECT id, name_gs, description_gs FROM g_sec"
                cursor.execute(sql1)
                dato=cursor.fetchall()
                users=[]
                for filas in dato:
                        user={'id':filas[0],'name_gs':filas[1],'description_gs':filas[2]}
                        users.append(user)
                return jsonify({'users':users,'resultado':"Usuarios."})
        except Exception as ex:
            return "Error"

@app.route('/challenge/GS/<name>',methods=['GET'])
def sg(name):
        try:
                cursor=conexion.connection.cursor()
                sql2="SELECT id, name_gs, description_gs FROM g_sec WHERE name = '{0}'".format(name)
                cursor.execute(sql2)
                data=cursor.fetchone()
                if data != None:
                        usergs={'id':data[0],'name_gs':data[1],'description_gs':data[2]}
                        return jsonify({'users':usergs,'resultado':"Usuario encontrado."})
                else:
                        return jsonify({'resultado':"Usuario no encontrado."})
        except Exception as ex:
                return "Error"


@app.route('/challenge', methods=['POST'])
def reg_us():
        try:
                cursor=conexion.connection.cursor()
                sqlp="INSERT INTO us_sec(name_alias,pass,create_time,status) VALUES ('{0}','{1}',{2},{3})".format(request.json['name_alias'],request.json['pass'],
                request.json['create_time'],request.json['status'])
                cursor.execute(sqlp)
                conexion.connection.commit()
                return jsonify({'resultado':"Usuario registrado."})
        except Exception as ex:
                return "Error"


if __name__ == '__main__':
    app.run(debug=True)


