tapioca = 4.50
salgado = 5.0
acai = 12.0

produto = input("digite 'S' para salgado ou 'T' para tapioca: ")
quant1 = int(input(""))
quant2 = int(input(""))
total_acai = acai * quant2
if produto.upper() == 'T':
	TOTAL = (tapioca * quant1) + total_acai
else:
	TOTAL = (salgado * quant1) + total_acai

print(round(TOTAL, 2))