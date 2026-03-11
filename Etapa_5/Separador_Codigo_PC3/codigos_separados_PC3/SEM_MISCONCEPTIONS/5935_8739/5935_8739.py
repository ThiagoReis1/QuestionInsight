quilo = float(input("peso da mercadoria a ser transportada: "))

valor = 43.21 * quilo

taxa = 25

total = valor + taxa

aumento = total + (total * (62/100))

print(round(aumento, 2))