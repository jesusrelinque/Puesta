def inversa (cadena):
    x = len(cadena)
    resultado = ""
    h = x
    for y in range(x):
        resultado += cadena[h-y-1]
    print (resultado)


cadena = "juanito"
inversa (cadena)
