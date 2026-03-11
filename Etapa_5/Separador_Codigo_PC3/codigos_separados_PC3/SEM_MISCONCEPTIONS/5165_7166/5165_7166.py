peso_racao = float(input("racao em gramas: "))
quantidade = float(input("quantidade diaria em gramas: "))
resto = peso_racao - (quantidade * 6)
print(round(resto, 4))