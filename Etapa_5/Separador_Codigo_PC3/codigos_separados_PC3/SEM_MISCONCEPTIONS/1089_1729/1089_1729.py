c1=int(input("informe o valor da primeira compra:"))
c2=int(input("informe o valor da segunda compra:"))
c3=int(input("informe o valor da terceira compra:"))
limite=input("informe limite:")
compra=c1+c2+c3
	print(round(compra,2))
if(compra>=900):
  	print("Sim")
else:
	print("Nao")