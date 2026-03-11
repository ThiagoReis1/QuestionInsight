#15 por hora
#5 taxa para limpeza
#20% adicional do total

tempo = int(input())

total = 15*tempo+5
total = total + (total*20/100)

print(round(total,2))