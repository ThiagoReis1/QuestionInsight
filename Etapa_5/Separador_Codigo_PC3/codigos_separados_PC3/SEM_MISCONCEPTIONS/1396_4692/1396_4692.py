valor=float(input("valor: "))
v1=(valor)+(valor/100)*10
v2=(valor)+(valor/100)*6
if(valor<=300):
	print(v1)
else:
	print(round(v2, 2))
