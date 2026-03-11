a = float (input ("Informe o preco da acao na abertura da bolsa: "))
f = float (input ("Informe o preco da acao no fechamento da bolsa: "))
x= f - a
x= (round (x,2))
if	(x>0):
	print ("saldo positivo")
elif	(x==0):
	print ("sem variacao")
elif	(x<0):
	print ("saldo negativo")