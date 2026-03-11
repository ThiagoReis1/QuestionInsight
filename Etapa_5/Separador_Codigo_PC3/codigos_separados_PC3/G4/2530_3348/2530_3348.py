D  = float(input("Deposito inicial: "))
TF = float(input("Tarifa mensal fixa: "))
j  = float(input("Taxa de juros: "))
saldo = D 
Dj = (D * 0.15) + D
t  = 0
if((D>0) and (TF>0) and (j>0)):
	while(saldo < Dj):
		renda = round((saldo + (saldo*(j/100))),2)
		saldo = renda - TF
		
		t = t +1
	print(t)	
else:
	print("Dados incorretos")

