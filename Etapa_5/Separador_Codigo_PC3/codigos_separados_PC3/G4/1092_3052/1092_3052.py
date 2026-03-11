e= int(input('Digite o numero aqui: '))
n1= e//100
r1= e%100
n2= r1//10
r2= r1%10
n3= r2//1

if (n1**3 + n2**3 + n3**3 == e):
	print (e)
	print ('atende')
else:
	print (e)
	print ('nao atende')