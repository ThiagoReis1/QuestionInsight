peso = float(input("Digite o peso da mercadoria a ser transportada: "))

quilo = 43.21
taxa = 25.0
total = (quilo * peso) + taxa

valor_total = (total * 0.62) + total

print(round(valor_total, 2))
