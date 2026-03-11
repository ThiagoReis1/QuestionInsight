valor=float(input("premio: "))
saque=float(input("saque: "))
juros=float(input("taxa de juros: "))/100
t=0
saldo=valor
p_premio=valor+valor*20/100
if(valor>0)and (saque>0) and (juros>0):
	while(saldo<p_premio):
		saldo=round((saldo+(saldo*juros)-saque),2)
		t=t+1
	print(t)
else:
	print("Dados incorretos")
	
	