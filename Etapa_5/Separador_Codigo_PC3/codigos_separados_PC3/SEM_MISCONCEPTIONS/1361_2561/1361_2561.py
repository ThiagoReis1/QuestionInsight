from math import sqrt

# Quantidade de poções, informada pelo usuário
pocoes = int(input())

# Quantidade de snowberry
print(round(pocoes * (sqrt(5) - 1) / 4, 2))

# Quantidade de sais de fogo
print(round(pocoes * (sqrt(5 - 2 * sqrt(5))), 2))

# Quantidade de amanita
print(round(pocoes * 5 * (5 - 2 * sqrt(5)), 2))