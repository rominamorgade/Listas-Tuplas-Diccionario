#Crea una tupla con los meses del año, pide números al usuario.
# si el número está entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición 
# sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero.

tupla_meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

while True:
    ingreso = input("Ingrese un número del 1 al 12 o un 0 para finalizar: ")
    if ingreso.isdigit():
        num = int(ingreso)
        
        if num == 0:
            print("Ingresaste 0. Ha finalizado el programa")
            break    
        
        elif 1 <= num <= len(tupla_meses):
            print(f"El mes {num} corresponde a: {tupla_meses[num - 1]}.")
 
        else:
            print("Error: valor inválido. Ingrese números entre 1 y 12")
    else:
        print("Valor inválido, ingrese solo números")        
        
        

        
    
        
    
    
    
    
   