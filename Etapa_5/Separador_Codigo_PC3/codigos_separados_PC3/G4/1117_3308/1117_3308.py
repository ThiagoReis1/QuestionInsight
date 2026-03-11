x =float(input("preco da entrada:"))
y = int(input("dia da semana:"))
c = input("digite se tem musica ao vivo:")
if((x>=0)and(1<y<7)and(c=="S")or(c=="N")):
	if(y==2)or(y==3)or(y==5):
		b= x-(x*25/100)
		print("Entradas:",x,",",y,",",c)
		print("Valor a pagar: R$",round(b,2))
	if(c=="S")and(1<y<7):
		d=(20.00+x)+(x-(x*25/100))
		print("Entradas:",x,",",y,",",c)
		print("Valor a pagar: R$",round(d,2))
else:
	print("Entradas:",x,",",y,",",c)
	print("Dados invalidos")