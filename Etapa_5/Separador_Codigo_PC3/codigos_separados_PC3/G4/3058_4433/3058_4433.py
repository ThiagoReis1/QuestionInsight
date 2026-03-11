area = float(input('digite a area: '))


if(area > 0 and area <=100):
	c = 2
	f = 100
	VT = area*c + f
	print(round(VT, 2))
elif(area > 100 and area <=2500):
	c = 1.8
	f = 150
	VT = area*c + f
	print(round(VT, 2))
elif(area > 2500 and area<=10000):
	c = 1.5
	f = 200
	VT = area*c + f
	print(round(VT, 2))
else:
	c = 1.2
	f = 250
	VT = area*c + f
	print(round(VT, 2))
	