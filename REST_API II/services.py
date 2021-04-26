from sqlite3 import Error

class Service_Sqlite:
    def __init__(self,conector):
        self._conector = self.sql_connexion();
        self._cursor = self.conector.cursor()    

    def sql_connexion(self):
        try:
            conexion = sqlite3.connect('all_data.db') # crea la base
            return conexion
        except Error:
            print(Error)
            
    def ejecutar_query(self,query):
            # execute a statement
        try:
            print('Ejecutando query...')
            self._cursor.execute(query) # cursor.execute("CREATE table personal(id integer PRIMARY KEY,descripcion text,salario integer)")
            print(query)
            print("Query ejecutado!")
            self._conector.commit()
        except:
            print("error en el query execution")
        
    def retornar_query(self,query):
        print('Ejecutando query...') # to check
        try:
            self._cursor.execute(query)
            print("Query ejecutado!") # if OK
            elementos = self._cursor.fetchall()
            return elementos;     
        except (Exception, psycopg2.Error) as error :
            print(error) # error code 500, error de servidor si desea.
            return respuesta # mensaje a regresar
 

    def insertar_new_register(self, valores):
        self._cursor.execute("INSERT INTO su_tabla_(_columna,_columna,_columna) VALUES(?,?,?)",valores)
        self._conector.commit()
        return respuesta # mensaje a regresar

    def todos_los_registros(self, table_id):
        table_name = "" # identificador para la tabla 
        self._cursor.execute("SELECT * FROM {}".format(table_name))
        resultado_de_query = cursor.fetchall() # todos los resultados
        elementos = [cada_registro for cada_registro in resultado_de_query] # para guardar cda/uno separado 
        return elementos
        
        