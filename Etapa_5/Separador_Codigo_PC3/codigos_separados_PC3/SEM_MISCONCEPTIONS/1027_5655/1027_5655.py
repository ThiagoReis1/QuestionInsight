kwh = float(input("kWh no mes: "))

consumo = 10.0 + (kwh * 0.43)
porc = consumo * 0.25
total = consumo + porc

print(round(total, 2))