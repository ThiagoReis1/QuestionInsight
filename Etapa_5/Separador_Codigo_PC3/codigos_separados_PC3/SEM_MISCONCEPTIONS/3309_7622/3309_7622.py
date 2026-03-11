peso = float(input("peso em kg da mercadoria: "))

frete = peso * 43.21 + 25
icms = frete / 100 * 62
total = frete + icms

print(round(total, 2))