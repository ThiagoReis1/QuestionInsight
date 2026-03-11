preco=float(input("digite o valor do preco: "))
codigo=input("digite o codigo:")
descontoBF=40/100
if(codigo=="1"):
	valorfrete=preco*10/100
elif(codigo=="2"):
	valorfrete=preco*8/100
elif(codigo=="3"):
	valorfrete=0
elif(codigo=="4"):
	valorfrete=preco*2/100

valor_da_venda=(preco-preco*descontoBF)+(valorfrete)
print(round(valor_da_venda,2))