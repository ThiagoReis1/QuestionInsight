p1= float(input("Preco da acao - abertura da bolsa:"))
p2= float(input("Preco da acao - fechamento da bolsa:"))
if(p1==p2):
	print("sem variacao")
elif(p1<p2):
	print("saldo positivo")
else:
	print("saldo negativo")