#valor de cada compra
valor_compra1= float(input())
valor_compra2= float(input())
valor_compra3= float(input())
#limite do cartao
limite= float(input())
#valor total
valor_total= valor_compra1 + valor_compra2 + valor_compra3
#condicoes
if (valor_total<= limite):
	print(round(valor_total, 2))
	print("Nao ultrapassou ")
else:
	print(round(valor_total, 2))
	print("Ultrapassou ")