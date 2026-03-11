kWh = float(input("Quantos kWh consumidos?"))
L = ((((kWh * 0.43) + 10) * 25/100) + ((kWh * 0.43)+ 10))
print(round(L, 2))