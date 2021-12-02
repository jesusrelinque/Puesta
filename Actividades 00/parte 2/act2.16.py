
print ("Que letra quieres?:")
letra = input()
def empieza (lista,letra):
    long=len(lista)
    cont=0
    resultado=""
    for x in range(long):
        cadena=lista[x]
        if cadena[0]==letra:
            cont+=1
            resultado+=cadena
            resultado+=", "
    print(f"La palabra: {resultado}empieza por {letra}, existen {cont}")

lista = ["pepe", "juan", "federico", "alfonso","pepepepe"]
empieza(lista,letra)