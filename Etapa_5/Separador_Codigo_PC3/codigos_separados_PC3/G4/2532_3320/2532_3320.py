vc=float(input("valor do carro: "))
vid=float(input("valor inicial do deposito: "))
dmf=float(input("deposito mensal fixo: "))
j=float(input("taxa de juros: "))
t=0
saldo=vid

if(vc>0 and vid>0 and dmf>0 and j>0 ):
	while(saldo<vc):
		saldo=saldo +saldo*(j/100)
		saldo=round(saldo,2)
		saldo=saldo+dmf
		t=t+1
		
	print(t)
else:
	print("Dados incorretos")