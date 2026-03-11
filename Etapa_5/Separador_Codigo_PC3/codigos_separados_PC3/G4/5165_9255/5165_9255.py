p = float(input("Peso da racao em gramas: "))
q = float(input("Quantidade diaria: "))
rest = p - (q * 6)

print(round(rest, 4))