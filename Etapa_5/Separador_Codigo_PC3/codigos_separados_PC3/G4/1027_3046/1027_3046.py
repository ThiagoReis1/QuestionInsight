l = float(input("informe o consumo de energia: "))

e = 10 + (l * 0.43)

icms = e * (25/100)

ct = e + icms
 
print(round(ct, 2))