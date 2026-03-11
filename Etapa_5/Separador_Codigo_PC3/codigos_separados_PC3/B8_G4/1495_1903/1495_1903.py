a = float(input("Digite a area: "))

if((a>=0) and (a<=10000)):
	c = 6
	f = 100
	t = (a*c)+f
	print(round(t,2))

elif((a>10000) and (a<=20000)):
	c = 5.5
	f = 150
	t = (a*c)+f
	print(round(t,2))

elif((a>20000) and (a<=30000)):
	c = 5
	f = 200
	t = (a*c)+f
	print(round(t,2))

elif(a>30000):
	c = 4.5
	f = 250
	t = (a*c)+f
	print(round(t,2))
