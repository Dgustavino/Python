"""Implemetacion del patron de comportamiento Adapter
"""

class MacDevice:
    """Mac commands"""
    def __init__(self):
        self.name = "Mac Computer"

    def command_ls(self):
        return "ls"


class WindowsDevice:
    """Windows commands"""
    def __init__(self):
        self.name = "Windows Computer"

    def command_dir(self):
        return "dir"


# aqui implemento el patron para solucionar los 
# comportamientos diversos de mis objetos para una misma accion

class Adapter:
    """Este constructor de clase recibe el objeto a adaptar
    y el metodo a adaptar como parametros, y los define genericos"""
    def __init__(self, object, **metodo_a_adaptar):
        self._object = object # object es una palabra reservada
        self.__dict__.update(metodo_a_adaptar) # this line transforms the generic method into the specific method

    def __getattribute__(self, atributo):   # accede a los atributos del objeto
        return getattr(self._object, atributo)


######################################################
lista_objetos_a_traducir = []

mac_computer = MacDevice()
PC_ = WindowsDevice()

lista_objetos_a_traducir.append(Adapter(mac_computer,fileLooker=mac_computer.command_ls()),Adapter(PC_, fileLooker=PC_.command_dir()))

print(Adapter.__dict__)

for device in lista_objetos_a_traducir:
    print("{} has used the command {}\n".format(device.name, device.fileLooker()))