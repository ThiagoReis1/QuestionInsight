peso = float(input("Digite o peso do saco de racao em gramas: "))
quant = float(input("Digite a quantidade diaria de racao em gramas: "))
resto = peso-quant*7
print(round(resto,3))
