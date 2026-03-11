opcao = input("Digite L para lanche ou S para salgado :")
quant = int(input("Digite a quantidade :"))
quant_refri = int(input("Digite a quantidade :"))

lanche = 5.00
salgado = 3.50
refrigerante = 4.00

if ( opcao == "L") :
	preco_final = (quant * lanche) + refrigerante * quant_refri
	print(round(preco_final, 2))
	
else:
	preco_final = (quant * salgado) + refrigerante * quant_refri
	print(round(preco_final, 2)) 