
# nested functions
def escribir_archivo(veces):
    # I/O  
    file_de_numeros = open('mi_primer_file.txt', 'w') 
    # asi creo un txt con permisos de escritura

    def multiplicar(veces):
        indice = 0
        resultados = []

        while indice !=5:
            resultados.append(indice*veces)
            indice = indice + 1
        
        return resultados

    file_de_numeros.write(str(multiplicar(veces)))
    file_de_numeros.close()

escribir_archivo(3)

def leer_archivo():
    with open('labs.txt', 'r') as mi_archivo_leido:
        print(mi_archivo_leido.read())
       # resultado = mi_archivo_leido.readlines()
       # print(type(resultado), str(len(resultado)), resultado[2]) 

leer_archivo()


""" Para curiosos """
# pueden investigar @decorators / wrap functions