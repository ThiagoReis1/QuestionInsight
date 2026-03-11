x= float(input("o consumo de energia de um cliente: "))

if(x<=150):
	y= (x*0.6)+5.0
else:
	y= (x*0.75)+16
	
print(round(y, 2))