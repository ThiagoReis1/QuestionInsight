d=float(input('Deposito inicial:'))
m=int(input('Numero de meses:'))
s=0
t=0
while(t<m):
	cre=d*0.01
	d=d+cre
	print(round(d,2))
	t=t+1
	