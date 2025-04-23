name = input("Digite seu nome: ")
salary = float(input("Digite seu salário: "))
bonus = float(input("Digite a porcentagem do bonus: %"))
CONST_BONUS = 1000
result = CONST_BONUS + salary * bonus

print(f"{name}, segundo os dados obtidos, o valor do seu bonus será: {result}")