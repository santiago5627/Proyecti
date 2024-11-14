import pymysql

miConnection = pymysql.connect (host='127.0.0.1', port= 3306, user = 'root', password = '', db = 'db_cardi')
cur = miConnection.cursor()

cur.execute("SELECT nombre FROM usuarioa")
for nombre in cur.fetchall():
    print(nombre)
    
miConnection.close()