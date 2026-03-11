quan = int(input(""))

if(quan < 17.5):
	x = quan + 1.5
	print(round(x, 1))
elif(quan >= 17.5) and (quan <= 35):
	x = quan + 2.3
	print(round(x, 1))
elif(quan >= 35) and (quan <= 50):
	x = quan + 3.3
	print( round(x, 1))
elif(quan >= 50):
	x = quan + 4.7
	print(round(x, 1))