x=float(input('Digite um numero real: '))
k=int(input('Digite um numero inteiro: '))
i=0
n=3
while (-1<=x<=+1) and (k>0):
	arctgx=x-(x**n/(n))*(-1**n)
	i=i+1
	n=n+2
	print(round(arctgx, 6))