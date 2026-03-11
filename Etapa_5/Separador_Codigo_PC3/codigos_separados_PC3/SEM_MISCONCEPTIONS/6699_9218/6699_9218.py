# entrada do tempo do estacionamento em horas

tempo = float(input("informe o valor de horas: "))

# total do gasto junto da taxa de limpeza
taxa = 15.00
limpeza = 5.00

total = tempo * taxa + limpeza

# total pago junto a porcentagem
total_pago = total + total * (20/100)

print(round(total_pago, 1))