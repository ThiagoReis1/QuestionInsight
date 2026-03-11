volume = float(input("volume consumido no mes:"))

m3 = 0.37

total = 15 + (0.37*volume)

pagar = total + total*(35/100)

print(round(pagar, 2))