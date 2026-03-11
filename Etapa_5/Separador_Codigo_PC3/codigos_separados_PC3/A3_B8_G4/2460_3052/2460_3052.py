a= float (input ('O preco da acao na abertura da bolsa: '))
f= float (input ('O preco da acao no fechamento da bolsa: '))

s= f - a

if (f > a):
	print ('saldo positivo')
elif ( f == a):
	print ('sem variacao')
elif (f < a):
	print ('saldo negativo')