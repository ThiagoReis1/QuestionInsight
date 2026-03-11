consumo = float(input("O consumo de chamadas (em minutos) durante certo mes: "))
m1 = consumo * 0.28 + 23
m2 = m1 * 0.31
valor = m1 + m2

print(round(valor, 2))