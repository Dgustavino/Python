# Programa Python para implementacion de MergeSort 

def mergeSort(arr): 
	if len(arr) >1: 
		mid = len(arr)//2 # Se parte el arreglo a la mitad 
		L = arr[:mid] # Se dividen los elementos de la matriz 
		R = arr[mid:] # en dos mitades(izq-der) 

		mergeSort(L) # Se ordena la primera mitad 
		mergeSort(R) # Se ordena la segunda mitad

		i = j = k = 0
		
		# Copia datos a matrices temporales L[] and R[] 
		while i < len(L) and j < len(R): 
			if L[i] < R[j]: 
				arr[k] = L[i] 
				i+= 1
			else: 
				arr[k] = R[j] 
				j+= 1
			k+= 1
		
		# Comprobando si queda algun elemento 
		while i < len(L): 
			arr[k] = L[i] 
			i+= 1
			k+= 1
		
		while j < len(R): 
			arr[k] = R[j] 
			j+= 1
			k+= 1

# Funcion para imprimir la lista 
def printList(arr): 
	for i in range(len(arr)):		 
		print(arr[i], end =" ") 
	print() 

 
if __name__ == '__main__': 
	arr = [12, 11, 13, 5, 6, 7] 
	print ("La matriz dada es:", end ="\n") 
	printList(arr) 
	mergeSort(arr) 
	print("La matriz ordenada es: ", end ="\n") 
	printList(arr) 


