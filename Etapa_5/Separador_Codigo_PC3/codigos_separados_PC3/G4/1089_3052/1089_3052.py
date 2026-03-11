#Entradas
c1 = float(input('valr da compra 1: '))
c2 = float(input('valr da compra 2: '))
c3 = float(input('valr da compra 3: '))
l= float(input('Qual o limite do cartao? '))
vtc= c1 + c2 + c3

if (vtc <= l):
	print (round(vtc,2))
	print ('Nao ultrapassou',)
else:
	print (round(vtc,2))
	print ('Ultrapassou')