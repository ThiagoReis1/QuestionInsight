#victor do vale moreira	
#07/07/2016
#av.02

compra_1 = float(input("Qual o valor da compra? "))
compra_2 = float(input("Qual o valor da compra? "))
compra_3 = float(input("Qual o valor da compra? "))
limite_cartao = float(input("Qual o limite?"))

valor_total = compra_1 + compra_2 + compra_3

if (limite_cartao >= valor_total):
	print(round(valor_total, 2))
	print("Sim")
else: 		
	print(round(valor_total, 2))
	print("Nao")