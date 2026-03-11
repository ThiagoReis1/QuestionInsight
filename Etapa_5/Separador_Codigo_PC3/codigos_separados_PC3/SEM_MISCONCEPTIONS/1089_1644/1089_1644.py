compra1=float(input("Qual o valor da compra?"))
compra2=float(input("Qual o valor da compra?"))
compra3=float(input("Qual o valor da compra?"))
limite=float(input("Qual o valor do limite?"))
valortotal= compra1+compra2+compra3
print(round(valortotal,2))

if(valortotal<=limite):
	print("Sim")
else:
	print("Nao")

