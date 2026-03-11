peso = float(input("peso da mercadoria a ser transportada: "))

quilo = float(43.21)
taxa = float(25)
icms = float(62 / 100)
preco = peso * quilo + 25
aumento = preco * icms

total = preco + aumento

print(round(total, 2))