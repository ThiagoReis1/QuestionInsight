d1=int(input('Valor do dado 1: '))
d2=int(input('Valor do dado 2: '))
r=int(input('Numero de rodada: '))

if((1>d1<6) or (1>d2<6) or (r<0)):
	print('Entrada invalida')
elif(d1+d2==12):
   print('CONSTRICAO')
   print(d1+d2+1)
else:
	(d1+d2>5)
   print('POLEN')
   print((d1+d2+1)*r)   
elif((d1+d2!=12) or (d1+d2<=5)):
	print('FRAQUEZA')
	print(d1*d2)


