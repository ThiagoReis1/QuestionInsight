vol = float(input("Volume de agua consumida no mes: "))
valf = 15.00
total = 0.37 * vol + valf
total2 = (35/100 * total) + total
print(round(total2, 2))