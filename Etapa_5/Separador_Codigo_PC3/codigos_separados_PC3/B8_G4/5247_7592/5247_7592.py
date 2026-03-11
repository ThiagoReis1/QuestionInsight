s = float(input("salario: "))
c = int(input("codigo"))

if(s>0)and((c==101)or(c==102)or(c==103)or(c==104)):
	if(c==101):
		d = (0.80/100)
		e = s * d
		f = s + e
		print("Novo salario: R$ ",round(f,2))

	elif(c==102):
		d = (0.65/100)
		e = s * d
		f = s + e
		print("Novo salaio: R$ ",round(f,2))

	elif(c==103):
		d = (0.60/100)
		e = s * d
		f = s + e
		print("Novo salario: R$ ",round(f,2))

	elif(c==104):
		d = (0.55/100)
		e = s * d
		f = s + e
		print("Novo salario: R$ ",round(f,2))
	
else:
	print("Dados invalidos")
	
