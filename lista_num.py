#Pedir números y meterlos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. Por último, muestra los números ordenados de menor a mayor.

lista_numeros = [] #Lista vacía para ir guardando los números durante la ejecución del programa 

while True:
    
    numero = int(input("Ingrese un número o 0 para salir: "))
    
    if numero == 0:
        print("Ingresó el número 0. El programa ha finalizado.")
        break  
    else:
        lista_numeros.append(numero)  # agrego los números a la lista

# Ordenamos los números de la lista de menor a mayor
lista_numeros.sort()

print("Éstos son tus números ordenados de menor a mayor:")
print(lista_numeros)