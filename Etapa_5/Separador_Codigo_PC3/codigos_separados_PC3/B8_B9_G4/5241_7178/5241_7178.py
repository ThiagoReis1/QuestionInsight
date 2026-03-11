a= int(input("consumo de agua: "))

if (a<10):
	y= (a*2)+20
	print(round(y,2))
elif ((a>=10) or (a<20)):
	y= (a*2.5)+20
	print(round(y,2))
elif ((a>=20) or (a<40)):
	y= (a*2.75)+20
	print(round(y,2))
elif (a>=40):
	y= (a*3)+20
	print(round(y,2))
