from math import *
#Captura de dados
p = float(input("Informe a massa da espada (em gramas): "))

#Processamento
flawless = 2**(1+(p/1000))

soul = p * ((pi**2)/3141)

dwarven = 2*(sqrt(p/40))

#Saída
print(round(flawless, 2))
print(round(soul, 2))
print(round(dwarven, 2))