precoKg = 43.21
taxa = 25.00
icms = 0.62

peso = float(input("Massa da mercadoria, em kg: "))
total = (peso * precoKg + taxa) * (1 + icms)
print(round(total, 2))