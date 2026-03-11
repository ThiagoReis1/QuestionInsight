sa = float(input('salario atual: '))
cod = int(input('codigo do cargo: '))
if (sa>0) and (cod==101 or cod==102 or cod==103 or cod==104):
	if cod==101:
		ns = (sa*0.008) + sa
		
	elif cod==102:
		ns = (sa*0.0065) + sa
		
	elif cod==103:
		ns = (sa*0.006) + sa
		
	elif cod==104:
		ns = (sa*0.0055) + sa
	print('Novo salario: R$',round(ns,2))
else:
	print('Dados invalidos')