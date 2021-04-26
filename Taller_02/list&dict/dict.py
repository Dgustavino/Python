# un dictionario se define asi KEY:VALUE
elemento = '02'

dict_musica = {
                'miKey': 1,
                'key_2': elemento,
                'key3': 3
                }

# print the OBJ dict
print(dict_musica)

# print a dictionary key:value
for key in dict_musica:
    print(key, dict_musica[key])

    # read specific key
print(dict_musica['key_2'])
    # adding a new Key
dict_musica['KEY4']=9

print(dict_musica)

my_tuplet1 = 1,'manzana'
my_tuplet2 = 2,'pera'
     # unpacking 
dict_frutas =  dict([my_tuplet1,my_tuplet2])
print(dict_frutas)

lista_duplicados = 1,2,2,3,3,4,5
lista_sin_duplicados = list(dict.fromkeys(lista_duplicados))
 # un approach para remover duplicados de una tupleta usando composicion
print(lista_sin_duplicados)
