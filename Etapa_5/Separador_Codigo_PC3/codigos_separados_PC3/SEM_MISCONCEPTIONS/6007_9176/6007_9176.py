espigas = float(input("Digite a quantidade de espigas de milho compradas: "))
if espigas >= 6:
 valor = 1.50
 total = valor * espigas
 print(round(total, 2))
else:
 valor = 1.85
 total = valor * espigas
 print(round(total, 2))

