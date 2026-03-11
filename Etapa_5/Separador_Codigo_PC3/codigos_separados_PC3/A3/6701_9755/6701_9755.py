valor = float(input("digite o valor total dos produtos: "))

frete = 15.00

juros = (30/100)

processo1 = valor+frete

processo2 = processo1+processo1*(30/100)

print(round(processo2, 2))