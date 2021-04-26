 # Programa en Python para demostrar
 # Duck Typing 


class Bird: 
	def fly(self): 
		print("fly with wings") 

class Airplane: 
	def fly(self): 
		print("fly with fuel") 

class Fish: 
	def swim(self): 
		print("fish swim in sea") 

# Los atributos que tienen el mismo nombre 
# son considerados como duck typing 
for obj in Bird(), Airplane(), Fish(): 
	obj.fly() 
