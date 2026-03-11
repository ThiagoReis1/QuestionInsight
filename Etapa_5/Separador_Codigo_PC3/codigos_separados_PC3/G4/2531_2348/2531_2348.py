v=float(input("valor do premio:"))
m=float(input("valor do saque:"))
j=float(input("juros:"))
a=j/100
t=0
saldo=v
if(v>0 and m>0 and j>0):
	while(saldo<(v+(v/100)*10)):
		saldo=saldo+saldo*a-m
		saldo=round(saldo,2)
		t=t+1
	print(t)
else:
	print("Dados incorretos")