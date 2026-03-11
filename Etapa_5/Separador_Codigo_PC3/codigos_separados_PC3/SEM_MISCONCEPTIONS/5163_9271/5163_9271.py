peso_em_gramas = float(input("Digite o peso do saco: "))
quantidade_de_racao_diaria = float(input("Digite a quantidade de racao: "))
numero_de_dias = 5
quantidade_restante = peso_em_gramas - (quantidade_de_racao_diaria * numero_de_dias)
print(round(quantidade_restante,3))