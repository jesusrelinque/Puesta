def mas_larga(lista):
    long = len(lista)
    resultado = lista[0]
    for x in range(long):
        if len(resultado) > len(lista[x]):
            resultado = resultado
        else:
            resultado = lista[x]
    print(f"La palabra con más caracteres es: {resultado}")

lista = ["pepe", "juan", "federico", "alfonso"]
mas_larga(lista)