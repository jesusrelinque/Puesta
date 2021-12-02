def vocal(x):
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        return True
    else:
        return False

if vocal("o"):
    print("Es vocal")
else:
    print("No es vocal")