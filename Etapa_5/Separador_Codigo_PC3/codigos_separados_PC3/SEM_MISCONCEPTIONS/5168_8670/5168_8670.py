peso = float(input("Informe o peso do saco de racao em gramas: "))
quantidade = float(input("Informe a quantidade diaria de racao em gramas: "))

x = peso - (quantidade * 7)

print(round(x,4))