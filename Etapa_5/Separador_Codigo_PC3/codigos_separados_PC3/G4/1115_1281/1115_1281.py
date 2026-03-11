s=float(input("Salario atual"))
c=int(input("Codigo"))
print("Entradas: R$", s, "e codigo", c)
if (s>0 and c==101 or c==102 or c==103 or c==104):
	if c==101:
		n=s+((0.80/100)*s)
	elif c==102:
		n=s+((0.65/100)*s)
	elif c==103:
		n=s+((0.60/100)*s)
	else:
		n=s+((0.55/100)*s)	
	print("Novo salario: R$", (round(n, 2)))
else:
	print("Dados invalidos")