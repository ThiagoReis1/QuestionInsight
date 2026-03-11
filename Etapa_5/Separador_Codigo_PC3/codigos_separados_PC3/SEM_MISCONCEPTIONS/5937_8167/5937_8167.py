precolitro = 2.86
servico = 50.00
quantlitros = float(input("Digite a quantidade de litros abastecidos: "))
total = precolitro*quantlitros + servico + 0.34*(precolitro*quantlitros+servico)
print(round(total,2))