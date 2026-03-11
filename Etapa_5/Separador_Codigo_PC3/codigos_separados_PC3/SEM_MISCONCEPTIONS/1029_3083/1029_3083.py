minutos = float(input("minutos: "))
consumo = minutos * 0.28 + 23.00
imposto = (consumo/100) * 31
total = consumo + imposto


print(round(total, 2))