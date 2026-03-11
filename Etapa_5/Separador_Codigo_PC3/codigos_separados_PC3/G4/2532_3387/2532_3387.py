c=float(input())
d=float(input())
m=float(input())
j=float(input())
j=j/100
i=0
soma=d
if	((c>0 and (m>0)and (j>0)and (d>0))):
	while	(soma<=0):
		acum=(soma+m)*j
		acum=round(acum,2)
		soma=soma+m+acum
		soma=round(soma,2)
		i=i+1
	print(i)
else:
	print("Dados incorretos")

		
		