abertura1 = float(input())
fechamento1 = float(input())

diferenca = fechamento1 - abertura1
percentual1 = (diferenca / abertura1)
percentual2 = percentual1 * 100

print(round(percentual2,2))