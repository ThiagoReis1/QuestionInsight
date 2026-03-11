a = float(input("Area:"))
if(a>=0):
	if(a>=0)and(a<=10000):
		print(round(a*6+100,2))
	elif(a>=10000)and(a<=20000):
		print(round(a*5.50+150,2))
	elif(a>=20000)and(a<=30000):
		print(round(a*5+200,2))
	elif(a>=30000):
		print(round(a*4.50+250,2))
		
		