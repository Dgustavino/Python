numero = int(7) # usando constructor int()

# diccionario
name_for_id = {
    302: 'Alicia',
    970: 'Bob',
    numero: 'James'
} # podemos usar una variable como key

def saludar(user_id): # utlizar el diccionario para personalizar un mensaje de saludo
    print("Hola %s" %name_for_id.get(user_id,"Personitas"))

saludar(970)