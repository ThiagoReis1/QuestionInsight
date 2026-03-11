p = float(input("peso da mercadoria em kg"))

kg = 43.21
taxa = 25.00
icms = 62/100

t = kg * p + taxa
v = (62/100)*t
total= t+v
print(round(total , 2))