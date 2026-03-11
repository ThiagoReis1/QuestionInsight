a= input('Nome do ácido')
if(a.upper() == 'GLUTAMINA'):
	c= 5*12.011+8*1.00794+14.0067+4*15.9994
	print(round(c,2))
elif(a.upper() == 'SERINA'):
	s= 3*12.011+7*1.00794+14.0067+3*15.9994
	print(round(s,2))
elif(a.upper() == 'TREONINA'):
	r= 4*12.011+9*1.00794+14.0067+3*15.9994
	print(round(r, 2))
else:
	print('Entrada: ',a)
	print('Dado Invalido')