v = float(input())
c = float(input())
j = float(input())
t = 0
saldo = v

if(v<=0 or c<=0 or j<=0):
	print("Dados incorretos")
else:
	while(saldo> (v/2)):
		rend = saldo * j/100
		saldo = round((saldo + rend) - c, 2)
		t = t + 1
	print(t)
		
		 
	


	
	