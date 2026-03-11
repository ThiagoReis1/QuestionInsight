p = float(input("Peso em gramas:"))
qd = float(input("Quantidade diaria:"))

s = (p * qd) - (p *(qd/6))

print(round(s,4))