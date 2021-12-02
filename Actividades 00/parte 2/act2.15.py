print ("Ingresa que edad quieres ver:")
edad = int(input())
def ver_mayor (edad,lista):
    long=len(lista)
    contador=0
    for x in range(long):
        if lista[x] > edad:
            contador+=1
    print(f"Existen: {contador} mayores de {edad} años")

lista=[3,64,48,19]
ver_mayor (edad,lista)

