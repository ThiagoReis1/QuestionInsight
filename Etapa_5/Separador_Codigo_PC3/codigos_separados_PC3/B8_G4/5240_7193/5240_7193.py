c = int(input("consumo de energia: "))

if (c<=100):
	x = c*0.50 + 50
elif (c>=100) and (c<250):
	x = c*0.75 + 50
elif (c>=250) and (c<500):
	x = c*1.00 + 50
elif (c>=500):
	x = c*1.25 + 50
	
print(round(x,2))