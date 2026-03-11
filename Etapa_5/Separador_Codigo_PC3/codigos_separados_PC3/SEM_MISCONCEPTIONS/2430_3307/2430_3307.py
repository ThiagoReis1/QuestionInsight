# Leitura do capital e tempo
capital = float(input('Valor total da compra: '))
tempo = int(input('Parcelas ao mes: '))

# Valores dos juros e montante
juros = (capital * 3 * tempo) / 100
m = capital + juros

print(round(m, 2))