d = float(input("deposito inicial: "))
tf = float(input("tarifa mensal: "))
j = float(input("taxa juros: "))
saldo = d
t = 0
v = (15/100)*d + d
if(d>0)and(tf>0)and(j>0):
	while(saldo<v):
		saldo = saldo + saldo* (j/100)
		saldo = round(saldo,2)
		saldo = saldo - tf
		t = t + 1
	print(t)
else:
	print("Dados incorretos")