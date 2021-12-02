def mayus (cadena):
    contador=0
    long=len(cadena)
    for x in range(long):
        h=cadena[x]
        if h == h.upper():
            contador+=1
    print(f"Existen: {contador} mayusculas")

cadena="PPepePepePEpe"

mayus(cadena)
