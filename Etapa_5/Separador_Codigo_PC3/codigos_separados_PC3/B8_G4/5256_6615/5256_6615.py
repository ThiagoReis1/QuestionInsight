a = float(input("digite o valor de abertura da acao: "))
f = float(input("digite o valor de fechamento da acao: "))

anls = f - a
if(anls==0):
	print("sem variacao")
else:
	if(anls>0):
		print("saldo positivo")
	elif(anls<0):
		print("saldo negativo")