x = int(input("insira o consumo de energia: "))
if(x<100):
	y = 0.50*x + 50
elif(100<=x<250):
	y = 0.75*x + 50
elif(250<=x<500):
	y = x*1 + 50
elif(x>= 500):
	y = x*1.25 + 50
print(round(y, 2))