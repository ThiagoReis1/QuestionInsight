volume = float(input("Quantidade gasta no mes: "))
valor = volume * 0.37 + 15.00
valort = valor * (35 / 100)
print(round(valor + valort, 2))