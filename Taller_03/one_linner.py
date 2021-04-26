# script de ejemplo para FOR de ONE LINNER

lista_numeros_for_regular = list()

for numero in range(0,5):
    lista_numeros_for_regular.append(numero*2)

# lista creada con el for regular con numeros 
# enteros del 0 al 5 multiplicados por 2
print(lista_numeros_for_regular)

                # [ logica  # elemento  # obj iterable ]
lista_for_one_linner = [num*2 for num in range(0,5)]   # -> mismo ejemplo para lambda

# lista creada con un for de one linner
print(lista_for_one_linner)

# script de ejemplo para un one linner con lambda
                        # argumento    #logica   # in linner for 
using_lambda_obj = lambda argumento: [argumento*num for num in range(0,5)]

#retorna el mismo resultado que las implementaciones anteriores
lista_lambda = using_lambda_obj(5)
print(lista_lambda)

################################################################################

              # mensaje es el argumento de la definicion de mi funcion
def mi_funcion(mensaje):    
    print(mensaje)
                # el proposito de poder usar "" o ''
    return ' Clase 4 "Mas conocimineto" de Progra  '

mi_funcion("Soy un parametro")"""

