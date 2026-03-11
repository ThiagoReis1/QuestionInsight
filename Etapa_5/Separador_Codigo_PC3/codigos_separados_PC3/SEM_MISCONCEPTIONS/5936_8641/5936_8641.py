kwh = float(input("consumo energia: "))

a = 0.43 * kwh 
b = 10.00
c = a + b
aumento = c * (25/100)
total = aumento + c

print(float(round(total, 2)))