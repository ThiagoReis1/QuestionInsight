peso = float(input("Qual o peso do saco de racao em gramas? "))
peso_diario = float(input("Qual o valor diario em gramas? "))
valor = (peso)-(peso_diario*7)
print(round(valor, 3))