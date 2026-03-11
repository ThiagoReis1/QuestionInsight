# Monalisa Pereira 21600560
# 16 06 2016
# Avaliacao 01 - Exercicio 02

encomenda = float(input("Insira valor da encomenda: "))

imposto = (encomenda / 100) * 81

taxa = 12.0

total = encomenda + imposto + taxa

print(round(total, 2))