x= input('e ? (T/S):')
qt= int(input('inserir a quantidade de T ou S:'))
ac= int(input('inserir a quantidade de ac:'))


if x=='T':
	tot1= 5.5*qt+10*ac
	print(round(tot1,2))
else:
	tot2= 4*qt+10*ac
	print(round(tot2,2))