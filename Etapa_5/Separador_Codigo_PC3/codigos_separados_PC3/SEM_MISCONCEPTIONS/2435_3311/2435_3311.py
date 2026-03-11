preco = float(input("Digite o preco original:"))
frete = preco * 0.05
precoDes = preco - (preco * (40/100))
print(round(precoDes,2))
print(round(frete,2))