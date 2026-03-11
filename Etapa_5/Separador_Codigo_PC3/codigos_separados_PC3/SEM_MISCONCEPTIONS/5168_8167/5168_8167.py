peso = float(input("Digite o peso do saco de racao em gramas: "))
quantidade_diaria = float(input("Digite a quantidade diaria de racao em gramas: "))
quantidade_restante = peso - (quantidade_diaria*7)
print(round(quantidade_restante,4))