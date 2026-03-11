peso = float(input("Digite o peso do saco de racao em gramas: "))
quantidade = float(input("Digite a quantidade diaria de racao em gramas: "))
qt_final = peso - (quantidade*5)

print(round(qt_final,2))