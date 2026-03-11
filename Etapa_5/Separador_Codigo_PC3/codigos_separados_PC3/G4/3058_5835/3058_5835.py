a=float(input("area:"))
if(a>0 and a<100):
	c=2
	f=100
	valor=a*c+f
elif(a>=100 and a<2500):
	c=1.8
	f=150
	valor=a*c+f
elif(a>=2500 and a<10000):
	c=1.5
	f=200
	valor=a*c+f
else:
	c=1.2
	f=250
	valor=a*c+f
print(round(valor, 2))