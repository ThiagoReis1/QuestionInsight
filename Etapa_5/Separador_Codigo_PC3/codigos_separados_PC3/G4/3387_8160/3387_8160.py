u= str(input('unidade(M/K): ')).upper()
v= float(input('valor: '))
if(u=='K'):
	mg=2.35215*v
	print(round(mg,2))
else:
	kl= v/2.35215
	print(round(kl,2))
	