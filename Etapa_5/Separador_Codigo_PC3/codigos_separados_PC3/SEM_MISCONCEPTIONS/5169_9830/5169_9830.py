peso = float(input("digite o peso de racao em gramas: "))
quantidade = float(input("digite a quantidade diaria de racao: "))

t = peso - (quantidade * 4)
print(round(t, 2))
