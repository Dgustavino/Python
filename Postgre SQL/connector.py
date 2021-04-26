import psycopg2
from psycopg2 import Error

class Conector():
    def start(self,conector):
        self._conector = conector;
        self._cursor = self.conector.cursor()    
        
    # para iniciar conexion con la DBA
    def connect(self):
        """ Connect to the PostgreSQL database server """
        try:
            # connect to the PostgreSQL server
            print('Conectando con PostgreSQL...')
            conexion = psycopg2.connect(host="localhost", database="dvdrental", user="postgres", password="123456")
            print('Conectado to the PostgreSQL DVDRENTAL DBA...')
            return conexion
        except (Exception, psycopg2.Error) as error :
            print ("Error conectando a PostgreSQL", error)


    def ejecutar_query(self,query):
        # execute a statement
        try:
            print('Ejecutando query...')
            self._cursor.execute(query)
            print(query)
            print("Query ejecutado!")
            self._conector.commit()
        except (Exception, psycopg2.Error) as error :
            print(error)
 
 
    def retornar_query(self,query):
        # execute a statement
        try:
            print('Ejecutando query...')
            self._cursor.execute(query)
            print("Query ejecutado!")
            elementos = self._cursor.fetchall()
            return elementos;      

        except (Exception, psycopg2.Error) as error :
            print(error)


if __name__ == '__main__':
    data_access_obj = Conector()
    conexion = data_access_obj.connect()
    data_access_obj.start(conexion)
    my_query = "select * from category;"
# objecto_conexion.ejecutar_query("CALL actualizalenguaje(2);")
    resultados = data_access_obj.retornar_query(my_query)
    print(resultados)