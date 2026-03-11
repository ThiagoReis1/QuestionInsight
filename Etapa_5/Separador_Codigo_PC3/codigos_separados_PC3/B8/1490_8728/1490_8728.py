v = float(input("volume:"))
if 0 <=v<=10:
	tarifa=3
	taxa=15
elif 10<v<=15:
	tarifa= 3.50
	taxa=20
elif 15<v<=20:
	tarifa=4
	taxa=25
elif 20<v:
	tarifa=4.50
	taxa=30
	
valor = v*tarifa+taxa
print(round(valor,2))
	