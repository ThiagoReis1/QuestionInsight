v = float(input("volume de agua consumido:"))
total = v*0.37 + 15
pagar = total + 35/100*total
print(round(pagar, 2))
