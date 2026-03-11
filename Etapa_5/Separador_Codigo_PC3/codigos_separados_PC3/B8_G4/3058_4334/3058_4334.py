a=int(input("Digite um numero que eh a area em m**2:" ))
#c eh o custo
#f eh o valor do fertilizante
#v eh o valor total
if(a>=0 and a<=100):
	c = 2.00
	f = 100.00
	v = (a * c) + f
	print(round(v,2))
elif (a>100 and a<=2500):
	c = 1.80
	f = 150.00
	v = (a * c) + f
	print (round(v,2))
elif (a>2500 and a<=10000):
	c = 1.50
	f = 200.00
	v = ( a * c) + f
	print (round(v,2))
elif (a>10000):
	c = 1.20
	f = 250.00
	v = (a * c) + f
	print (round(v,2))
		