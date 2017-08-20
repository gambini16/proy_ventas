import mysql.connector


def conexion():
    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="ventas")
    return con
