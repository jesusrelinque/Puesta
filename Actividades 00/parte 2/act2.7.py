def superposicion (list1,list2):
    long1 = len(list1)
    long2 = len(list2)
    for x in range(long1):
        for y in range (long2):
            if list1[x] == list2[y]:
                h=x
                h+=1
                print(f"Hay una coincidencia en: {list1[x]} de la lista 1 en la posición {h}")


lista = ["pepe", "juan", "federico", "alfonso"]
lista2 = ["pepe", "paco", "marta", "federico"]

superposicion(lista,lista2)