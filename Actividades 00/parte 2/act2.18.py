def bisiesto (ano):
    con1 = ano%4
    con2 = ano%100
    if con1 == 0 and con2 != 0:
        print(f"El año: {ano} es bisiesto")
    else:
        print(f"El año: {ano} no es bisiesto")
print ("Ingresa un año:")
ano = int(input())
bisiesto(ano)