def binario(num):
    con = 0
    long = len(num)
    h = long
    for x in range(long):
        con +=(pow(2, x) * int(num[h-x-1]))
    print(con)

binario("1101101")