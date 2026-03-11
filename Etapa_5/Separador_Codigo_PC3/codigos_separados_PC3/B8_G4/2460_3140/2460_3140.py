bi=float(input("abertura da bolsa"))
bf=float(input("fechamento da bolsa"))

p=bf-bi

if(p>0):
	print("saldo positivo")
elif(p==0):
	print("sem variacao")
elif(p<0):
	print("saldo negativo")