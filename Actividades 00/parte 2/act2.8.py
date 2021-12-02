def generar_n_caracteres(num,carac):
    resultado=""
    for x in range(num):
        resultado += carac
    print (resultado)

generar_n_caracteres(4,"*")