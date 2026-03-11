a=float(input("salario atual: "))
b=int(input("codigo: "))

print("Entradas: R$", a, "e codigo", b )

if  ((a > 0) and (b == 101) or (b == 102) or (b == 103) or (b == 104)):
	if(b == 101):
		c=(a*(0.80/100))+a
		print("Novo salario: R$",round(c,2)) 
	elif(b == 102):
		d=(a*(0.65/100))+a
		print("Novo salario: R$",round(d,2)) 
	elif(b == 103):
		e=(a*(0.60/100))+a
		print("Novo salario: R$",round(e,2) )
	elif(b == 104):
		f=(a*(0.55/100))+a
		print("Novo salario: R$",round(f,2) )
else:
	print("Dados invalidos")