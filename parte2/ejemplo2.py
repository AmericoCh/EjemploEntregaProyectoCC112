# Escribimos en el archivo
with open('archivo1.txt', 'w') as archivo:
    archivo.write("Hola Mundo !.\n")
    archivo.write("Estamos escribiendo en el archivo.\n")

# Leemos  un archivo
with open('archivo1.txt', 'r') as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)

# Añadir texto al archivo
with open('archivo1.txt', 'a') as archivo:
    archivo.write("Añadiendo texto al archivo.\n")
