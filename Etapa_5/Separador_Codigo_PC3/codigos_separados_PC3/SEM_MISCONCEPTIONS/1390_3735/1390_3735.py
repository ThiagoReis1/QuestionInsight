var1= int(input("Consumo:  "))
if(var1<=100):
	tarifa= 1.20 * var1
else:
	tarifa= 25 + var1*1.40
print(round(tarifa, 2))


