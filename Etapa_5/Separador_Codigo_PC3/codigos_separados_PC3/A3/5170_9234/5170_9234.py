pesoracao = float(input("digite o saco em gramas: "))
quantdiaria = float(input("quantidade diaria de racao em gramas: "))
total = pesoracao-(quantdiaria*7)
total2 = total*7/7
print(round(total, 3))