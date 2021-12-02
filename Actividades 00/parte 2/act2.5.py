def suma (lista):
    resultado = 0
    x = len(lista)
    for y in range(x):
        resultado += lista[y]

    print (f"La suma de los números da: {resultado}")

def multiplicar (lista):
    resultado = 1
    x = len(lista)
    for y in range(x):
        resultado *= lista[y]

    print (f"La suma de los números da: {resultado}")
lista = [1,2,3,4]
suma (lista)
multiplicar (lista)