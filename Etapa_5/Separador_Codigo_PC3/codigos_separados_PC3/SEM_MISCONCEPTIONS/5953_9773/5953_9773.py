lp=input()
lp=lp.upper()
if lp=='P':
	quant_lp=int(input())
	quant_refri=int(input())
	valor=quant_lp*13.5+quant_refri*3
	print(valor)
if lp=='L':
	quant_lp=int(input())
	quant_refri=int(input())
	valor=quant_lp*6+quant_refri*3
	print(valor)
