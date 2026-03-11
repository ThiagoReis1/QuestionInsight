capital = float(input())
tempo = float(input())
taxa_juros = 3

juros = (capital * taxa_juros * tempo) / 100

round(juros,2)

montante = capital + juros

print(round(montante,2))
