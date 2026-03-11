D = float(input())
TF = float(input())
j = float(input())/100
t=0
saldo = D - TF + j
while(saldo > D + D *15/100):  
	if(D>0 and TF>0 and j>0):
		t=t+1
		saldo = -TF + j
		round(saldo,2)
	else: 
		print("Dados incorretos")
print(t)
