c= float(input())
d= float(input())
m= float(input())
j= float(input())
saldo = d
t= 0
if ((c>0) and (d>0) and (m>0) and (j > 0)):
	while(saldo < c):
		saldo = saldo +  saldo * j/100 + m
		saldo = round(saldo,2)
		t = t + 1
	print(round(t,2))
else:
	print("Dados incorretos")
