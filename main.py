import math

date = input("Insira uma data no formato (dd/mm/yyyy): ")
formated_date = date.split("/")
print(f"Dia: {formated_date[0]} - Mês: {formated_date[1]} - Ano {formated_date[2]}")
