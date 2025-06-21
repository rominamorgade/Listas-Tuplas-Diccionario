#Vamos a declarar un diccionario para guardar los precios de las distintas frutas.
# El programa pedirá el nombre de la fruta y la cantidad que se ha vendido
# y nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario.

precios_f = {
    "manzana": 250,
    "naranja": 170,
    "banana" : 400
}

nombre = input("Ingrese el nombre de la fruta: ")
cantidad_vendida = input("Ingrese la cantidad vendida: ")

if cantidad_vendida.isdigit():
    cantidad = int(cantidad_vendida)
    
    match nombre:
        case "manzana":
            precio_final = precios_f["manzana"] * cantidad 
            print(f"El precio final de las frutas vendidas es de: {precio_final}")
        case "naranja":
            precio_final = precios_f["naranja"] * cantidad  
            print(f"El precio final de las frutas vendidas es de: {precio_final}")
        case "banana":
            precio_final = precios_f["banana"] * cantidad  
            print(f"El precio final de las frutas vendidas es de: {precio_final}")    
        case _:
            print("Esa fruta no está en nuestro registro.")
   
else:
    print("Valor inválido. Ingrese solo números." )    

   