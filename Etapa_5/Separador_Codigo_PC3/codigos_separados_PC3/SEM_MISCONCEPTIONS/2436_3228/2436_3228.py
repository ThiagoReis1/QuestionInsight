pesokg = float(input())
distanciakm = float(input())
precokg = pesokg * 25.00
precokm = distanciakm * 0.12
icms = (precokg + precokm) * 0.12
total = (precokg + precokm) + icms

print(round(total, 2