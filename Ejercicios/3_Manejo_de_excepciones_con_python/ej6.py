import mysql.connector

try:
    cnx = mysql.connector.connect(user='usuario', password='contraseña',
                                host='localhost',
                                database='basededatos')

    cursor = cnx.cursor()

    cursor.execute("SELECT * FROM tabla_inexistente")

except mysql.connector.Error as err:
    print("Ha ocurrido el siguiente error con la base de datos: {}".format(err))

