# verificar si un número es par o impar
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# imprime los pares e impares entre 1 y 10
for i in range(1, 11):
    if es_par(i):
        print(f"{i} es par")
    else:
        print(f"{i} es impar")