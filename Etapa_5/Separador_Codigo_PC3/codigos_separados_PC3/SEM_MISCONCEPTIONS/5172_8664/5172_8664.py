# 1 - peso do saco de ração em gramas.
# 2 - quantidade de ração em gramas.

peso = float(input("Qual o peso do saco de racao em g?"))
qtd = float(input("Qual o a quatidade de racao em gramas? "))

total = peso-(qtd*5)

print(round(total, 2))

