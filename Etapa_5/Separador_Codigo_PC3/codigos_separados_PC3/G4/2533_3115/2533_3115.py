v = float(input(""))
c = float(input(""))
j = float(input(""))
p = j/100

t = 0
saldo = v
if(v<=0 or c<=0 or j<=0):
	print("Dados incorretos")
	exit()
else:
	
	while(saldo>v/2):
		
		saldo = saldo + (saldo*p) - c
		t = t + 1
	print(t)
		