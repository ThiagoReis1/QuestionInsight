x=float(input("horas"))
if(x<=20):
	pag=50*x
else:
	e=x-20
	pag=50*20+70*e
print(round(pag,2))