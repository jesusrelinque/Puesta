print ("¿Dime un número?")
num1 = int(input())
print ("¿Dime otro número?")
num2 = int(input())
if num1 > num2:
    print(f"El número mayor es: {num1}")
elif num2 > num1:
    print(f"El número mayor es: {num2}")
else:
    print(f"Los dos números son iguales")