peso = float(input("Informe o peso do saco de racao (em gramas):"))
quantidade = float(input("Informe a quantidade diaria de racao (em gramas): "))

tempo_de_consumo = 6

quantidade_de_racao = peso - quantidade * tempo_de_consumo

print(round(quantidade_de_racao, 4))