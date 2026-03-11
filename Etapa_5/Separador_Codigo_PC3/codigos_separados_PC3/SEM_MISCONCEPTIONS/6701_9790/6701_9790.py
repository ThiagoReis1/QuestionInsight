produtos = int(input("valor: "))
frete = produtos + 15
total = produtos + 15 + frete * (30/100)
print(round(total, 2))