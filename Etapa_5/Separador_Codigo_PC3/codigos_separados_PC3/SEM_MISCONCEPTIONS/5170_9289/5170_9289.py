peso_em_gramas = float(input("Peso em gramas: "))
quantidade_diaria = float(input("Quantidade diaria de racao: "))

quantidade_restante = peso_em_gramas - (quantidade_diaria * 7)


print(round(quantidade_restante, 3))
