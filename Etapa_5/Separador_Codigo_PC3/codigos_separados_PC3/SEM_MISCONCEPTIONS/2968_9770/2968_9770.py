ls=input()
ls=ls.upper()
if ls == 'S':
	quant_ls = int(input())
	quant_refri=int(input())
	valor=quant_ls * 3.50 + quant_refri * 4
	print(valor)
if ls == 'L':
	quant_ls=int(input())
	quant_refri=int(input())
	valor  =quant_ls * 5 + quant_refri*4
	print(valor)