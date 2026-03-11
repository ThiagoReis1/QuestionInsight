V=float(input())
M=float(input())
j=float(input())
j1=j/100
t=0
saldo=V
if(V<=0)or(M<=0)or(j<=0):
	print("Dados incorretos")
else:
	while(saldo<(0.2)*V):
		saldo = saldo + saldo*j1
		saldo = round(saldo,2)
		V=V+saldo-M
		t=t+1
	print(t)

	
	