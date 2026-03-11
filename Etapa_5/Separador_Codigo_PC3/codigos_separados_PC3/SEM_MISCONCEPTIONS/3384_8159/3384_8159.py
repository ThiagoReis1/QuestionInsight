uni_m=input("Ubidade de medida: (O ou Z) ").upper()
if(uni_m=="O"):
	oz=float(input("valor de medida: "))
	kg=oz/35.274
	print(round(kg,2))
else:
	kg=float(input("valor da medida: "))
	oz=35.274*kg
	print(round(oz,2))