maca= float(input("digite o numero de maca compradas: "))
uni= 0.30
des= 0.25
duzia= 12

if maca<duzia:
	valortotal= maca * uni
else:
	valortotal = maca * des
	
print(round(valortotal, 2))