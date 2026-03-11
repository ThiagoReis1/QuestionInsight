p = float(input("peso = "))

frete = p * 43.21 + 25 

valor_total = frete + (frete * 0.62)

print(round(valor_total, 2))