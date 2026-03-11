peso=float(input(""))
fixo=60
if peso<50:
	total=fixo+4.50
elif peso==50:
	total=fixo+5.50
elif peso>50:
	total=fixo+6.50
print(round(total,2))