c=int(input("consumo de agua "))
if(c<10):
	total=20+2*c
	print(round(total,2))
elif((c>=10) and (c<20)):
	total=20+2.5*c
	print(round(total,2))
elif((c>=20) and (c<40)):
	total=20+2.75*c
	print(round(total,2))
else:
	total=20+3*c
	print(round(total,2))