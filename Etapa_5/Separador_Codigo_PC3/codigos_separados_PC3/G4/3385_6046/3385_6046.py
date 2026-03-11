#acre = 2,47105*Ha

U= input("unidade em que a medida esta Aacre ou Hhectares): ")
v= float(input("valor da medida: "))

if U=="A":
	h= v/2.47105
	print(round(h, 2))
if U=="H":
	a= 2.47105* v
	print(round(a, 2))
	

