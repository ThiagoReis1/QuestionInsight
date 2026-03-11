x=input("Aminoacido: ").upper()

if(x=='ALANINA'):
	p=3*12.011+7*1.00794+14.00674+2*15.9994
	print(round(p,2))
elif(x=='VALINA'):
	p=5*12.011+11*1.00794+14.00674+2*15.9994
	print(round(p,2))
elif(x=='TIROSINA'):
	p=9*12.011+11*1.00794+14.00674+3*15.9994
	print(round(p,2))
else:
	print("Entrada:",x)
	print("Dado Invalido")