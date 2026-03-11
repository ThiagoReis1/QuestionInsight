x=float(input("area a ser coberta: "))

if((x>=0)and(x<=100)):
	c=2.00
	f=100.00
	v=(x*(c))+f
	print(v)
elif((x>100)and(x<=2500)):
	c=1.80
	f=150.00
	v=(x*(c))+f
	print(v)
elif((x>2500)and(x<=10000)):
	c=1.50
	f=200.00
	v=(x*(c))+f
	print(v)
elif(x>10000):
	c=1.20
	f=250.00
	v=(x*(c))+f
	print(v)
