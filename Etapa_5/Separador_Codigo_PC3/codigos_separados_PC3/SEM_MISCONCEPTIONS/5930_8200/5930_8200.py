encomenda = float(input('qual o valor da encomenda ? '))
taxa = encomenda * (81 / 100)
frete = 12.

total = encomenda + taxa + frete 

print(round(total, 2))