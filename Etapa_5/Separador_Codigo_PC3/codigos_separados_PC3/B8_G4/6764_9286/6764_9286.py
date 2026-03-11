p = float(input("Peso da carga:"))
if(p<5):
	t = 10.00+3.75
	print(round(t,2))
elif (p==5):
	t = 10.00 + 4.75
	print(round(t,2))
elif (p>5):
	t = 10.00 + 5.75
	print(round(t,2))
	
	
	