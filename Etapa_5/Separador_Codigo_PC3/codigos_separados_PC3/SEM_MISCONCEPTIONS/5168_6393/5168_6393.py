# Objetivo = Determina a quantidade de dias que a reção durará

# Ler as entradas de peso de ração em gramas e quantidade diaria de ração em gramas para os três passaros

peso = float(input("Digite o peso em gramas: "))
quantidade = float(input("Quantidade de ração em gramas: "))

# Calcular 

total = peso - (quantidade * 7)

# Print saida

print(round(total,4))