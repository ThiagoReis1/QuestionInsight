
produtos = float(input("Digite o valor dos produtos: "))

frete = 15

valor_produtos = produtos + frete

icms = valor_produtos * (30/100)

valor_total = valor_produtos + icms

print(round(valor_total,2))
