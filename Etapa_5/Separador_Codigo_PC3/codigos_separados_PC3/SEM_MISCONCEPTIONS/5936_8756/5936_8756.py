kWh = float(input("kWh:"))

gasto = kWh * 0.43 + 10
Total = gasto * (25/100)

tudo = gasto + Total

print(round(tudo,2))