qnt = float(input("Quantos litros foram abastecidos? "))

lg = 2.86
to = 50
icms = ((qnt * lg) + to) * (34/100)
ser = (qnt * lg) + to
total = icms + ser

print(round(total, 2))