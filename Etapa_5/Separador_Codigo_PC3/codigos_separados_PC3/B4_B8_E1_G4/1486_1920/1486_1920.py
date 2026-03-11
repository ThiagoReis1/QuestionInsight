i = input("INGREDIENTE: ").upper()
qt = int(input("Quantidade(g):"))
if (i=='ARROZ' or i=='CENOURA' or i=='KAMPYO'\
or i=='NORI' or i=='OMELETE' or i=='PEPINO'\
or i=='SALMAO' or i=='SHITAKE'):
#tested before here
	if(qt<0 or qt>10000):
		print('Entrada invalida')
	else:
		#determinar numero de sushis
		if (i=='ARROZ'):
			print(qt//500)
		elif (i=='CENOURA'):
			print(qt//100)
		elif (i=='KAMPYO'):
			print(qt//20)
		elif(i=='NORI'):
			print(qt//50)
		elif (i=='OMELETE'):
			print(qt//200)
		elif (i=='PEPINO'):
			print(qt//150)
		elif (i=='SALMAO'):
			print(qt//300)
		elif (i=='SHITAKE'):
			print(qt//150)
#tested 1if 2if 1else
else:
	print('Entrada invalida')