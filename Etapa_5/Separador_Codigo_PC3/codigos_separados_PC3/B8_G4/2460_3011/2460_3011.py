a=float(input("Abertura da Bolsa:"))
f=float(input("Fechamento da Bolsa:"))
p=round(f-a,2)
if(not(p==0)):
	if(p>0):
		print("saldo positivo")
	elif(p<0):
		print("saldo negativo")
else:
	print("sem variacao")