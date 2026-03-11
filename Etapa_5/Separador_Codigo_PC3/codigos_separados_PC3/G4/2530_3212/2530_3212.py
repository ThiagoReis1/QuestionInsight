D=float(input("deposito inicial:"))
TF=float(input("tarifa mensal:"))
j=float(input("juros:"))

saldo=0
t=0


while (saldo>D):
	if(D<=0 and TF<=0 and j<=0):
		print("Dados incorretos")
	else:
		y=(D+D*(j/100))-TF
		saldo=round(saldo+y,2)
		t=t+1
print(t)