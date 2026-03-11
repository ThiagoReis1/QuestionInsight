d = float(input())
tf = float(input())
j = float(input())
saldo = d
t = 0

if(d > 0 and tf>0 and j>0):
	
	while(saldo < (d + (d*15/100))):
		saldo = saldo + (saldo*j/100)
		saldo = saldo - tf
		t = t + 1
		saldo = round(saldo, 2)
		
	print(t)
	
else:
	print("Dados incorretos")