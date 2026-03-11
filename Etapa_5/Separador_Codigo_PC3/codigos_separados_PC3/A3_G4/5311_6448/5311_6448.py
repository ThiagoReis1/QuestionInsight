di=float(input("Deposito inicial: "))
mes= int(input("Qte meses: "))
rend=0
mes=1
#juros=0.012
while (mes<=12):
	rend= rend + di*0.012
	mes=rend + 1
	print(round(mes,2))	
