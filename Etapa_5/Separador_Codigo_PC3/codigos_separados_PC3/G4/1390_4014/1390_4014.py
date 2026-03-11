c=float(input("consumo: "))
if(c<=100):
	t= c * 1.20
	print(round(t, 2))
else:
	t1= (c*1.40) +25
	print(round(t1, 2))