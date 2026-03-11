kwh = float(input("consumiu em um mes"))

icms = 25 / 100

conta_de_energia = (0.43 * kwh + 10.0) * icms

valor_total = (0.43 * kwh + 10.0 + conta_de_energia)

print (round(valor_total, 2))