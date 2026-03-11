peso = float(input("peso do saco de racao em g: "))
quantidade = float(input("quantidade diaria em g: "))

racaof = peso - (quantidade * 7)

print(round(racaof, 3))