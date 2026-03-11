c= float(input())
d= float(input())
m= float(input())
j= float(input())
meses = 1
soma = d
if ( not(c<0) or (d<0) or (m<0) or (j<0)):
	while(soma < c):
		soma = round(soma + m * (m * j/100),2)
		meses = meses + 1
	print(meses)
else:
	print("Dados incorretos")