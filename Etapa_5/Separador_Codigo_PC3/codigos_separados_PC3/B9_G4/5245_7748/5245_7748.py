s= float(input('salario:'))

if s<=0:
	print('Dado invalido')
	
else:
	if s <=800:
		ns= round(s*50/100+s,2)
		print('Novo salario:','R$',ns)
	else:
		if s>800 and s<=1000:
			ns= round(s*40/100+s,2)
			print('Novo salario:','R$',ns)
		else:
			if s>1000 and s<=1200:
				ns= round(s*30/100+s,2)
				print('Novo salario:','R$',ns)
			else:
				if s>1200 and s<=1400:
					ns= round(s*20/100+s,2)
					print('Novo salario:','R$',ns)
				else:
					if s>1400 and s<=1600:
						ns= round(s*10/100+s,2)
						print('Novo salario:','R$',ns)
					else:
						ns= round(s*5/100+s,2)
						print('Novo salario:','R$',ns)