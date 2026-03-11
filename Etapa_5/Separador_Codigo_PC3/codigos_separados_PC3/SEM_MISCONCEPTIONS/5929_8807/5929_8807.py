volume = float(input("Volume de agua consumida: "))
taxa = 15
valor = (volume * 0.37 + taxa) + (volume * 0.37 + taxa) * 35/100

print(round(valor, 2))