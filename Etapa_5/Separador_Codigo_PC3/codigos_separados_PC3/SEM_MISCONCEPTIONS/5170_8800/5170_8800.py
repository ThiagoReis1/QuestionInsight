peso = float(input("digite o peso do saco: "))
quantidade = float(input("digite a quantidade diaria de racao: "))

quantidade_racao = peso - (quantidade * 7)

print(round(quantidade_racao, 3))