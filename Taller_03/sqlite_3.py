import sqlite3 as dba_object 
from sqlite3 import Error

""" siempre necesitamos un 'string connection' para formalizar
el vinculo con el motor de base de datos"""
#_CONSTANTE_STRING_CONNECTION = ['Username', 'password', 'nombre_dba'] 
#_CONSTANTE_MODELADO_QUERIES = "select {} from {} where {}".format(value1,value2,value3)

def sqlite_create_database():
    try:
        conexion = dba_object.connect("mi_primera_base_datos.db")
        return conexion
    except Error as err:
        print(err)


def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE personal_adm(_id INTEGER PRIMARY KEY, puesto TEXT, salario INTEGER)")
        connection.commit()
    except Error:
        print(Error, "Debio ser en el query!")


def insertar_new_row(connection, valores):
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO personal_adm(_id,puesto,salario) VALUES(?,?,?)", valores)
        connection.commit()
    except Error:
        print(Error, "Debieron ser valores erroneos!")


def actualizar_registro(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE personal_adm SET salario=2300000 WHERE _id=123")
        connection.commit()
    except Error:
        print(Error, "Debieron ser valores erroneos!")

############################## IMPLEMENTACION DE LAS FUCIONES ANTERIORES:

objeto_conexion = sqlite_create_database()
create_table(objeto_conexion)

# creo tupletas con los valores a inyectar en mi query de INSERT
valores_1 = (123,'Profesor', 8000)
valores_2 = (777, 'Directora', 300000)
valores_3 = (555, 'Programador', 9)
         # _id (int PK), puesto(TEXT), salario(INTEGER)

valores_dict = {
        1: valores_1,
        2: valores_2,
        3: valores_3
}

# Inyecto INSERT INTO table con valores pretederminados
for key in valores_dict:
    print(valores_dict[key])
    insertar_new_row(objeto_conexion, valores_dict[key])


def get_all_rows(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM personal_adm") # SOLO EJECUTA
        objeto_resultado = cursor.fetchall() # TODOS LOS REGISTROS QUE DEVOLVIO EL QUERY
        connection.commit()

        return objeto_resultado

    except Error:
        print(Error, "Debieron ser valores erroneos!")

resultado = get_all_rows(objeto_conexion)

for item in resultado:
    print("REGISTRO: ", item)

actualizar_registro(objeto_conexion)

# 
resultado = get_all_rows(objeto_conexion)

for item in resultado:
    print("REGISTRO: ", item)