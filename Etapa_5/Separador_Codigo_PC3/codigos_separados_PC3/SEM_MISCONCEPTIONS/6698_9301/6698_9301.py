praca = float(input("pracas: "))



soma = (praca * 9.80) + 20.0
juros = (15/100) * soma
total = (soma + juros)

print(round(total, 2))