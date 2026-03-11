peso = float(input("Digite o peso do saco de racao em gramas: "))
quantidade = float(input("Digite a quantidade diaria de racao em gramas: "))

q_racao = peso - (quantidade * 4)

print(round(q_racao, 2))