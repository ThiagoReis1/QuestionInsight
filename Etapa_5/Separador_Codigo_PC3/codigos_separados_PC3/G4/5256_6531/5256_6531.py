x = float(input("Preco da bolsa: "))
y = float(input("Preco da acao: "))

c = round(y - x, 2) 

if( c > 0):
   print("saldo positivo")
elif(c == 0):
	print("sem variacao")
else:
	print("saldo negativo")
