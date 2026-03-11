consumo = float(input("Consumo mensal : "))
preco = consumo * 0.43
preco_parcial = preco + 10.00
preco_total = preco_parcial + (preco_parcial * (25/100))
print(round(preco_total,2))