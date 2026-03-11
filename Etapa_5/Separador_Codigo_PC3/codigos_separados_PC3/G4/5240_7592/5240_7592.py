a = int(input("consumo"))

if(a<100):
	b = 0.5
	c = a * b
	
elif(250>a>=100):
	b = 0.75
	c = a*b
	
elif(500>a>=250):
	b = 1
	c = a*b
	
elif(a>=500):
	b = 1.25
	c= a * b
	
else:
	print("invalido")

print(round(c,2) + 50)