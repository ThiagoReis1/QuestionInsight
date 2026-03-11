peso = float(input("peso do saco de racao: "))
quantidade = float(input("quantidade diaria de racao: "))

qtd = quantidade * 4
total = peso - qtd
print(round(total, 2))