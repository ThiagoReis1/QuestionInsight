tempo = float(input("tempo de estacionamento: "))

taxa = tempo * 15 + 5
gasto_total = (taxa * 20/100) + taxa

print(round(gasto_total, 2))
