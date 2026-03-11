peso_do_saco_de_racao = float(input("Peso do saco de racao em gramas"))
quantidade = float(input("Quantidade diaria de racao em gramas"))
quantidade_restante = peso_do_saco_de_racao - quantidade * 7
print(round(quantidade_restante, 4))


