k = float(input("Quantos kWh consumiu no mes?"))

t = (k * (0.43) + 10 )  
vt = t + (t * (25/100))
print(round(vt,2))