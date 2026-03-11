valor_pedagio = 9.80
taxa_manutencao_estradas = 20.00
ICMS = 15 #Porcentagem

quantidade = int(input("Informe a quantidade de pracas de pedagio no caminho: "))

total_gasto = valor_pedagio * quantidade + taxa_manutencao_estradas

valor_total = total_gasto + total_gasto * ICMS / 100

print(round(valor_total, 2))