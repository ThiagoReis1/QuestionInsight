tempo = float(input("Digite o tempo gasto: "))

valor = 0.28 * tempo + 23.00
impostos = 0.31 * valor

total = valor + impostos

print(round(total, 2))