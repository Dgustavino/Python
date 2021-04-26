# Programa Python para implementacion de QuickSort 

# Esta función toma el último elemento como pivote, lugares
# el elemento pivote en su posición correcta en orden
# array, y coloca todos los más pequeños (más pequeños que el pivote)
# a la izquierda del pivote y todos los elementos mayores a la derecha
# del pivote

def partition(arr,low,high): 
	i = ( low-1 )		 # índice de pivote de elemento más pequeño
	pivot = arr[high]	 

	for j in range(low , high): 

		# Si el elemento actual es más pequeño que el pivote 
		if arr[j] < pivot: 
		
			# incrementa el indice del elemento mas pequeño
			i = i+1
			arr[i],arr[j] = arr[j],arr[i] 

	arr[i+1],arr[high] = arr[high],arr[i+1] 
	return ( i+1 ) 

# La funcion principal que implementa QuickSort 
# arr[] --> Array para ordenar, 
# low --> Indice inicial, 
# high --> Indice final 

# Funcion  Quick sort 
def quickSort(arr,low,high): 
	if low < high: 

		# pi es el indice de particion, arr[p] esta ahora 
		# en el lugar correcto 
		pi = partition(arr,low,high) 

		# Ordenar por separado los elementos antes
		# de la partición y después de la partición
		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high) 


arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Matriz ordenada:") 
for i in range(n): 
	print ("%d" %arr[i]), 
 
