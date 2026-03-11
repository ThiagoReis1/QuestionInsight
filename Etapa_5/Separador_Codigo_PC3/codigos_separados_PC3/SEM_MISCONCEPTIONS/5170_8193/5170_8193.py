peso = float(input("peso_da_racao:"))
quantidade = float(input("quantidade_de_racao:"))

total = quantidade*7
total2 = peso - total

print(round(total2, 3))
