x=float(input( ))
d=int(input( ))
m=input( )

y=(75/100)
t=x*y
w=round(t,2)
r=x+20
z=round(r,2)
s=y*r
j=round(s,2)

print("Entradas:",x,",",d,",",m)

if x>=0:
	if m=="N":
		if d==1:
			print("Valor a pagar: R$", x)
		elif d==2:
			print("Valor a pagar: R$",w)
		elif d==3:
			print("Valor a pagar: R$", w)
		elif d==4:
			print("Valor a pagar: R$", x)
		elif d==5:
			print("Valor a pagar: R$", w)
		elif d==6:
			print("Valor a pagar: R$", x)
		elif d==7:
			print("Valor a pagar: R$", x)
		else:
			print("Dados invalidos")
	elif m=="S":
		if d==1:
			print("Valor a pagar: R$", z)
		elif d==2:
			print("Valor a pagar: R$", j)
		elif d==3:
			print("Valor a pagar: R$", j)
		elif d==4:
			print("Valor a pagar: R$", z)
		elif d==5:
			print("Valor a pagar: R$", j)
		elif d==6:
			print("Valor a pagar: R$", z)
		elif d==7:
			print("Valor a pagar: R$", z)
		else:
			print("Dados invalidos")
	else:
		print("Dados invalidos")
else:
		print("Dados invalidos")

