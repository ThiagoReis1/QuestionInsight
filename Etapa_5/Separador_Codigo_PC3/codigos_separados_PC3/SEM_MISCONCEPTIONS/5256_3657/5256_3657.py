entrada=float(input("De a entrada: "))
saida=float(input("De a saida: "))
entrada=round(entrada,2)
saida=round(saida,2)
x=saida-entrada
if(x>0):
	print('saldo positivo')
elif(x<0):
	print('saldo negativo')
else:
	print('sem variacao')
	