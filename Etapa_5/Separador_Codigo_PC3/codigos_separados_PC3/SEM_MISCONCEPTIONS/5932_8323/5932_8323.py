consumo = float(input("Consumo mensal em minutos: "))
taxa = (consumo * 0.28) + 23
total = taxa + taxa * 0.31

print(round(total, 2))