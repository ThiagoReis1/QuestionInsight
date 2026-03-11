p = float(input("Peso da mercadoria transprotada: "))

frete = p * 43.21 + 25.0 
icms = 62/100 * frete
total = frete + icms

print(round(total, 2))