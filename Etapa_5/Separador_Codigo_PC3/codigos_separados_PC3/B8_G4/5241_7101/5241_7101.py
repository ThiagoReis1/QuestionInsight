agua = int(input("Consumo de agua: "))
if (agua<10):
	v = agua*2+20
	print(round(v,2))
elif (10<=agua<20):
	v = agua*2.5+20
	print(round(v,2))
elif (20<=agua<40):
	v = agua*2.75+20
	print(round(v,2))
elif(40<=agua):
	v = agua*3+20
	print(round(v,2))
					  