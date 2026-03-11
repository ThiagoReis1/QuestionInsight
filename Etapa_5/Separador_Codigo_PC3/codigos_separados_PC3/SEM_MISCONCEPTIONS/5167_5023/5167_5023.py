peso = float(input("Peso do saco de racao: "))
quantidade = float(input("Quantidade diaria de racao: "))
total1 = 7 * quantidade
total2 = peso - total1
print(round(total2,3))