import math

try:
    n1 = int(input("Insira um numero inteiro: "))
    n2 = int(input("Insira outro numero inteiro: "))
    result = n1 // n2
    print(result)
except TypeError as error:
    print(error)
else:
    print("successfully script")
finally:
    print("finally script")