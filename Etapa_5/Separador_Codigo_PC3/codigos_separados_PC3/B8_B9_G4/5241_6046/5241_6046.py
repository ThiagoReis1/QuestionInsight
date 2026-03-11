ca= int(input("consumo de agua: "))

if ca<10:
	tca= (2*ca)+20
	print(round(tca, 2))
elif ca>=10 and ca<20:
	tca= (2.5*ca)+20
	print(round(tca, 2))
elif ca>=20 and ca<40:
	tca= (2.75*ca)+20
	print(round(tca, 2))
elif ca>=40: 
	tca= (3*ca)+20
	print(round(tca, 2))