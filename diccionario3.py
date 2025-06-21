#Vamos a declarar un diccionario para guardar los precios de las distintas frutas.
# El programa pedirá el nombre de la fruta y la cantidad que se ha vendido
# y nos mostrará el precio final de la fruta a partir de los datos guardados en el dicciona

precios_f = {
    "manzana": 240,
    "naranja": 170,
    "banana": 400
}

nombre = input("Ingrese el nombre de la fruta: ")
cantidad_vendida = input("Ingrese la cantidad vendida: ")

if cantidad_vendida.isdigit():
    cantidad = int(cantidad_vendida)

    
    if nombre == "manzana":
        final = precios_f["manzana"] * cantidad
        print(f"El precio final de la venta es de: {final} pesos")
    

    elif nombre == "banana":
        final = precios_f["banana"] * cantidad
        print(f"El precio final de la venta es de: {final} pesos")

    elif nombre == "naranja":
        final = precios_f["naranja"] * cantidad
        print(f"El precio final de la venta es de: {final} pesos")

    else:
        print("Lo siento, no tenemos esa fruta.")

else:
    print("Por favor, ingresá un número válido para la cantidad.")
