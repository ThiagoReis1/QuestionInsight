bp=float(input("Base maior: "))
bm=float(input("Base menor: "))

al=float(input("Altura: "))

custo=float(input("Custo de servico: "))

formula = (al * (bp+bm)) /2

final = formula * custo

print(round(final,2))