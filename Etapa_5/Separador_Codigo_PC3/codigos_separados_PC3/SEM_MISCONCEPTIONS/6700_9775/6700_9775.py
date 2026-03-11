aluguel = 50
taxa = 30

dias = float(input('Dias de esprestimo: '))

valor_ini = (aluguel * dias) + taxa
valor_fin = valor_ini + (valor_ini * 18/100)

print(round(valor_fin, 2))