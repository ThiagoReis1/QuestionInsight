x = float(input("horas trabalhadas: "))

if(x>=0 and x<=10):
	pag = x*50.00 + 500.00
	print(round(pag,2))
elif(x>10 and x<=20):
	pag = x*60.00+600.00
	print(round(pag,2))
elif(x>20 and x<=30):
	pag = x*70.00+700.00
	print(round(pag,2))
elif(x>30):
	pag = x*80.00+800.00
	print(round(pag,2))