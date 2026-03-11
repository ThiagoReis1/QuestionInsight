kwh = float(input("qtde de kwh: "))

total = (kwh * .43 + 10)
total2 = (total * 25 / 100) + total

print(round(total2, 2))