peso = float(input('informe o peso do saco de racao, em gramas: '))
quantidade = float(input('quantidade diaria racao, em gramas: '))

quantidade_dias = 5 * quantidade

print(round(peso - quantidade_dias, 2))