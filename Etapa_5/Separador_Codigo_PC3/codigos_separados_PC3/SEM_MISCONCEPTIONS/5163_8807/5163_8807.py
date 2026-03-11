peso = float(input("Qual o peso do saco de racao? "))
quantidade = float(input("Qual a quantidade de racao? "))

restante = peso - quantidade * 5

print(round(restante, 3))