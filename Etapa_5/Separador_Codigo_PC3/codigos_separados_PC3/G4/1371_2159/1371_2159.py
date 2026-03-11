# Quantidade de Antídoto
ant = float(input("Digite a quantidade de antídoto: "))

# Porcentages
pcas = 11.05/100
palh = 17.68/100
poleo = 71.27/100

# A quantidade de ingredientes
cas = (pcas*ant)
alho = (palh*ant)
oleo = (poleo*ant)

# Resultado
print(round(cas,2))
print(round(alho,2))
print(round(oleo,2))
