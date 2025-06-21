precios_f = {
    "manzana": 240,
    "naranja": 170,
    "banana": 400
}

nombre = input("Ingrese el nombre de la fruta: ")
cantidad_vendida = input("Ingrese la cantidad (x unid.) vendida: ")


if cantidad_vendida.isdigit():
    cantidad = int(cantidad_vendida)

    if nombre == "manzana" or nombre == "banana" or nombre == "naranja":
        final = precios_f[nombre] * cantidad 
        print(f"El precio final de la venta es de: {final} pesos")
        
    else:
        print("Esa fruta no está en nuestro registro.")
else:
    print("Valor inválido. Ingrese solo números.")



