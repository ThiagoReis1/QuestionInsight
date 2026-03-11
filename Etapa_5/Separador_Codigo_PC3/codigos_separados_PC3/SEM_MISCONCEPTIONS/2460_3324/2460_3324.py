abertura= float(input())
fechamento= float(input())
dif= fechamento-abertura
percentual= (dif*100/abertura)

if(percentual>0):
	print("saldo positivo")
elif(percentual<0):
	print("saldo negativo")
else:
	print("sem variacao")
	
	