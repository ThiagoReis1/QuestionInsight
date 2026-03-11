pesomercadoria = float(input("O peso da mercadoria a ser transportada: "))

quilo = 43.21
taxa = 25

custo = (pesomercadoria * quilo) + taxa

total = (custo *(62/100)) + custo

print(float(round(total, 2)))
