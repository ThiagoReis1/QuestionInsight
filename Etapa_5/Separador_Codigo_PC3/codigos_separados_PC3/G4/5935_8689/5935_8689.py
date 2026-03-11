#calculo do frete

p = float(input("informe o peso da mercadoria em kg:"))
k = (p * 43.21) + 25
v = k * (62 / 100)
taxa = k + v

print(round(taxa, 2))