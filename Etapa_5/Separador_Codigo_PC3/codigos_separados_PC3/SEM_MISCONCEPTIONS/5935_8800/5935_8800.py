kg = float(input("digite o peso da mercadoria: "))
frete = (43.21 * kg) + 25
icms = frete * 0.62
total = frete + icms
print(round(total, 2))