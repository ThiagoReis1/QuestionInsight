preco = 0.28
fixo = 23.00
taxa = 31.0/100
minutos = float(input("minutos: "))
valor = (preco*minutos)+fixo
total = valor+valor*taxa
print(round(total,2))