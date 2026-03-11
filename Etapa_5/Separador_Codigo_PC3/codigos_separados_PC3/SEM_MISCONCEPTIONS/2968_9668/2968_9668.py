lanc_salg= input("L para lanche ou S para salgado: ").upper()
quant_lanch_salg= int(input("quantidade lanche salgado: "))
quant_refri= int(input("quantidade de refris: "))

lanche= 5.00
salgado= 3.50
refri= 4.00

if lanc_salg == "S":
	tot_salg= (quant_lanch_salg * salgado ) + (quant_refri * refri)
	print(round(tot_salg, 2))
	
else:
	tot_lanch= (quant_lanch_salg * lanche) + (quant_refri * refri)
	print(round(tot_lanch, 2))