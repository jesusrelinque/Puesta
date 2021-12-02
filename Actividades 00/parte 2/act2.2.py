def max_de_tres(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(f"El número mayor es: {num1}")
    elif num2 > num1 and num2 > num3:
        print(f"El número mayor es: {num2}")
    elif num3 > num1 and num3 > num2:
        print(f"El número mayor es: {num3}")
    else:
        print(f"Los tres números son iguales")

print ("¿Dime un número?")
num1 = int(input())
print ("¿Dime otro número?")
num2 = int(input())
print ("¿Dime el último número?")
num3 = int(input())
max_de_tres(num1, num2, num3)