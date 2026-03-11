mercadoria = float(input("digite o peso do produto: "))
frete = mercadoria*43.21 +25.00
total = frete + frete*(62/100)
print(round(total, 2))
