unid = input(" ")
med = float(input("insira um numero: "))

if ( unid == 'M'):
	K = (med/2.35215)
	print(round(K, 2))
else: 
	M = (2.35215 * med)
	print(round(M, 2))