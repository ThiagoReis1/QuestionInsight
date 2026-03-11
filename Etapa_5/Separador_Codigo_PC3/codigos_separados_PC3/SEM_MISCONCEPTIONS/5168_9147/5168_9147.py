peso = float(input("Digite o peso do saco de racao (em g): "))

quantidade_de_racao_diaria = float(input("Digite a quantidade diaria de racao (em g): "))

restante = peso - (quantidade_de_racao_diaria * 7)

print(round(restante, 4))
