m=float(input("minutos de voo: "))
if(m<=200):
	total=5000+100*m
	print(round(total,2))
if(m>200):
	total=8000+(90*(m-200))+100*200
	print(round(total,2))