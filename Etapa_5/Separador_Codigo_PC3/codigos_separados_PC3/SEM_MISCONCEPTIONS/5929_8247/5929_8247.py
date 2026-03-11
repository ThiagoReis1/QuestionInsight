vol = float(input("Insira o volume de agua consumida durante o mes: "))
valor = 15 + 0.37*vol
total = valor*35/100 + valor
print(round(total, 2))