d= float (input("deposito inicial: "))
m = float (input ("meses de aplicacao: "))
i=0
t = d
while(i < m):
	t = t + t*0.01
	i=i+1
	print(round(t, 2))