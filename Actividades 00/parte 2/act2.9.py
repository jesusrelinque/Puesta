def generar_n_caracteres(num,carac):
    resultado=""
    for x in range(num):
        resultado += carac
    print (resultado)
def procedimiento(lista):
    long=len(lista)
    for x in range(long):
        num=lista[x]
        generar_n_caracteres(num,"*")

lista = [1,6,3,6]
procedimiento(lista)
