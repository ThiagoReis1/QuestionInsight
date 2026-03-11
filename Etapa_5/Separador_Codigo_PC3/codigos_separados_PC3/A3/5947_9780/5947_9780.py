pedido= input ("C OU E: ")
quant= int(input())
quant_sucos = int(input())

valor_coxinhas = 2.00
valor_esfirras = 4.50
valor_sucos = 6.00

if pedido == "C":
	total = (quant * 2.00)
else:
	total= (quant * 4.50)
total2= total+ (quant_sucos * 6.00)
print(round(total2,2))