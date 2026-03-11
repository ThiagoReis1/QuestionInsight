item = input().upper()
quant_item = int(input())
quant_capp = int(input())

if item == "B":
	valor = 3.0*quant_item + 5.5*quant_capp
else:
	valor = 6.0*quant_item + 5.5*quant_capp

print(round(valor,2))