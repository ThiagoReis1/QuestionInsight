peso_racao = float(input("Digite a quintidade de ração em gramas: "))
quantidade_diaria = float(input("Digite a quantidade diaria de ração: "))

total_semanal = quantidade_diaria * 7
resto_semanal = peso_racao - total_semanal

print(round(resto_semanal,4))