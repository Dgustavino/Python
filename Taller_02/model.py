""""Estructura de una aplicación MVC
Definición de Modelos
Modelo: Incluye todos los datos y su lógica relacionada.

Definicion de Vistas
Vista: presentar datos al usuario o manejar la interacción del usuario (entrega las entradas del usuario)

Definición de controladores
Controlador: una interfaz entre los componentes Modelo y Vista"""


class Student():
    """bluePrint of a stundent"""

    def __init__(self,numEstu,nombre):
        self.numEstu=numEstu
        self.nombre=nombre
        print("Cod: {} / Nombre: {}".format(self.numEstu,self.nombre))

