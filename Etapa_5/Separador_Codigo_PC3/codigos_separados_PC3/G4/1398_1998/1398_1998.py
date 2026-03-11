x = float (input ("Digite o tempo de voo: "))
if (x<=200) :
	y = round(5000 + 100*x,2)
	print (y)
if (x>200) :
	z = round(8000 + 20000 + 90*(x-200),2)
	print (z)