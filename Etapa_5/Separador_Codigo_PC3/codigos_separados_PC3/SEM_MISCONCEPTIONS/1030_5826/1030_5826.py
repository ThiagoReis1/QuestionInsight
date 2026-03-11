minutos = float(input("Digite o total de minutosexcedentes: "))

plano = (45 + 0.97*minutos)
juros = 0.42 * plano

total = plano + juros

print(round(total,2))