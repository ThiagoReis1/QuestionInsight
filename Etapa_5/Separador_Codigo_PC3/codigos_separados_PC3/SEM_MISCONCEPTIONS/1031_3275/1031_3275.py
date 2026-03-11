litros=float(input())

precolitros = litros * 2.86
trocadeoleo = 50.00
totalservico = (precolitros + trocadeoleo)
total = totalservico + (totalservico * 0.34)

print(round(total,2))