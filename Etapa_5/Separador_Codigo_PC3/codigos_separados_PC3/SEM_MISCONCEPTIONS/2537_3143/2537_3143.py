V = float(input("valor da heranca :"))
M = float(input("saque mensal :"))
J = float(input("taxa de juros :")) /100
saldo = V
t = 0
if ( V > 0 and M > 0 and J > 0)
	while(saldo <= 0.20 * V + V ):
		saldo = saldo + (J * saldo) - M	
		t = t + 1
   print(t)
else:
	print("Dados")
	
	