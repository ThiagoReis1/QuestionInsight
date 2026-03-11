valor=float(input("Digite o valor de x: "))

if(valor<=-1 or valor >=1):
	print(valor*valor)
elif(valor>-1 and valor<0 or valor>0 and valor<1):
	print(valor)
elif(valor==0):
	print(1)
else:
	print(round(valor, 4))