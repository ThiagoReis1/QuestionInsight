k = float(input("Quantos kWh foram consumidos: "))
total = (k*0.43)+10

icms = total*(25/100)
l = total+icms
print(round(l,2))