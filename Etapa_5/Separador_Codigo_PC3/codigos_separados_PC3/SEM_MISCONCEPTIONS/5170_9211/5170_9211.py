peso = float(input("peso do saco de racao"))
quantidade = float(input("quantidade diaria de racao"))
sobra = peso - (quantidade * 7)
print(round(sobra,  3))