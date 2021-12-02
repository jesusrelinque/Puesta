def max(num):
    long=len(num)
    resultado = num[0]
    for x in range(long):
        if resultado > num[x]:
            resultado = resultado
        else:
            resultado=num[x]
    print(f"El número mayor es: {resultado}")

lista=[3,6,256,9]
max(lista)

