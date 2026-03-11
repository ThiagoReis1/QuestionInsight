p = float(input("Insira o peso da racao em gramas:"))
q = float(input("Insira a quantidade diaria em gramas:"))

r = p-q*6

print(round(r, 4))

p%(q*6)