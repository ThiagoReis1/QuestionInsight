valor = float(input())
tempo = int(input())
taxas = 3
Juros = (valor * taxas * tempo) / 100
M = valor + Juros
print(round(M,2))
