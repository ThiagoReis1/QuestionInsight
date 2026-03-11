nr = float(input('Valor: '))
ni = float(input('Valor: '))
soma = 1
cont = 0
if -1 < nr < 1 and ni > 0:
	while cont < ni:
		d = (-1)**(cont + 1)
		e = (nr**(cont + 1))
		f = d*e
		soma = soma + f
		cont+=1
	soma = 1/soma
	soma = soma -1
		
	print(round(soma, 7))								
		
	