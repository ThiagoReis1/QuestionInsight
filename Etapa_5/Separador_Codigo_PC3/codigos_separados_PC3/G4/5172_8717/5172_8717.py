p = float(input("Peso do saco em gramas: "))
qnt = float(input("Quantidade de racao em gramas: "))

qr = p - (qnt*5)

print(round(qr, 2))