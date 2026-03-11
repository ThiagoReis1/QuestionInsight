tapioca = 5.50
salgado = 4.00
acai = 10.00

pedido = input("Digite (T) se sua escolha for tapioca, (S) se for salgado: ")
quant = int(input("Agora informe a quantidade desejada do seu pedido anterior: "))
quantacai = int(input("Aqui informe quantos Acai ira pedir: "))

if pedido .upper() == "T":
	conta = (tapioca*quant)+(quantacai*acai)
	print (round(conta,2))
else:
	conta = (salgado*quant)+(quantacai*acai)
	print (round(conta, 2))
	
