vel=int(input())
temp=float(input())
print("Entradas:", vel,"km/h e", temp, "h")
if vel<100 and temp<=1:
	print("Proxima parada: Bravos")
elif vel>=100 and temp>1:
	print("Proxima parada: Castamere")
elif vel<=100 and temp>=4:
	print("Proxima parada: Doriath")
elif vel>100 and temp<4:
	print("Proxima parada: Doriath")
elif vel<=100 and temp>=6:
	print("Proxima parada: Edoras")
elif vel>100 and temp<6:
	print("Proxima parada: Edoras")
elif vel<=100 and temp>=7,5	