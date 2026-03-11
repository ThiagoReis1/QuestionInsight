x = float (input ("Informe o preco normal da entrada: "))
y = int (input ("Informe o dia da semana: "))
z = (input ("Eh dia de musica ao vivo, S ou N? "))


print ("Entradas:",x,",", y,",", z)
if	(x>=0)and((y==1)or(y==2)or(y==3)or(y==4)or(y==5)or(y==6)or(y==7))and((z=="S")or(z=="N")):
	if	((y==2)or(y==3)or(y==5))and(z=="N"):
		a = x-(x*(25/100))
		print ("Valor a pagar: R$", round(a, 2))
	elif	((y==1)or(y==4)or(y==6)or(y==7))and(z=="N"):
		print ("Valor a pagar: R$", round (x, 2))
	elif	((y==1)or(y==4)or(y==6)or(y==7))and(z=="S"):
		d = x + 20 
		print	("Valor a pagar: R$", round (d, 2))
	elif	((y==2)or(y==3)or(y==5))and(z=="S"):
		c = x-(x*(25/100))
		b = c + 20
		print ("Valor a pagar: R$", round (b, 2))
else:
	print ("Dados invalidos")			 