# peso do saco de ração em gramas
P = float(input("Digite o peso do saco de racao: "))

# quantidade diária de ração em gramas
Qnt = float(input("Digite a quantidade diaria de racao: "))

# quantidade de ração em gramas após 5 dias
resto = P - (5 * Qnt)

# resultado
print(round(resto,2))