from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app= Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'challenge'

conexion = MySQL(app)

app.secret_key = "llavesecreta"


@app.route('/')
def Index():
    cur = conexion.connection.cursor()
    cur.execute('SELECT * FROM us_sec')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', users = data)

@app.route('/add_us', methods=['POST'])
def add_us():
    if request.method == 'POST':
        namea = request.form['namealias']
        password = request.form['password']
        time=request.form['fdc']
        estado=request.form['status']
        cur = conexion.connection.cursor()
        cur.execute("INSERT INTO us_sec (name_alias, pass, create_time, status) VALUES (%s,%s,%s,%s)", (namea, password,time,estado))
        conexion.connection.commit()
        flash('Usuario agregado satisfactoriamente')
        return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)
