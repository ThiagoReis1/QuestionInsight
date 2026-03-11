d = float(input())
tf = float(input())
j = float(input())
saldo = d
i = 0
if (d >0 and tf > 0 and j >0):
	while (saldo < d + (d*0.15)):
			saldo = (saldo + (saldo *(j/100)))- tf
			i = i +1
	print(i)
else:
	
	print("Dados incorretos");