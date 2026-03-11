peso_saco_gramas = float(input())
quantidade_diaria = float(input())

gasto_semanal = quantidade_diaria*7
result = peso_saco_gramas - gasto_semanal
print(round(result, 4))