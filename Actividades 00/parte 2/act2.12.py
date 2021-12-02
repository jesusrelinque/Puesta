def filtrar_palabras(lista,num):
    long = len(lista)
    resultado=""
    coma=", "
    for x in range(long):
        if len(lista[x])>num:
            resultado+=lista[x]
            resultado += coma
    print(f"Las palabras que tiene más caracteres que {num} son: {resultado}")


lista = ["pepe", "juan", "federico", "alfonso","pepepepe"]
filtrar_palabras(lista,5)