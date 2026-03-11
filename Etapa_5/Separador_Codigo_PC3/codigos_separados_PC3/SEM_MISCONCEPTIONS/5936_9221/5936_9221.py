valorFixo= 10.00
consumoMes= float(input("digite o consumo do mes:"))
kwh= 0.43
total= valorFixo + (consumoMes* kwh)
total1= total+total*25/100
print(round(total1, 2))
