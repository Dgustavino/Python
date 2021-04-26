lista_ejemplo_numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,29]

# " for each " dentro de un Obj Iterable
for numero in lista_ejemplo_numeros:
    print(numero)

# podemos recorrer listas por la instruccion [start:stop:step]
print(lista_ejemplo_numeros[::-3])
                                   # los indices negativos van en reversa
print(lista_ejemplo_numeros[4]) # acceder por indice
                                 
lista_ejemplo_numeros.append(5689) # append me ingresa un elemento al final de la lista

     # pop saca el ultimo elemento de la lista y lo devuelve
print(lista_ejemplo_numeros.pop())

     # index me da el indice del elemento 
print(lista_ejemplo_numeros.index('abc'))

                # constructor list()
lista_normal = list()


contador = 0
# como llenar una lista manualmente
while contador < 10:
    lista_normal.append(0)
    contador=contador+1

varr='elemento' 

lista_normal[1]=varr # asigar valor al indice

# reversa el objeto actual 
lista_normal.reverse()

# copy devuelve una lista exactamente igual
lista_reversada = lista_normal.copy()

# devolvemos el objeto a su estado original
lista_normal.reverse()

# imprimimos las listas
print(lista_normal,lista_reversada)