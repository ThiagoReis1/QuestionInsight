item= input("L ou P").upper()
quant = int(input("quant de lanche de prato: "))
qrefri= int(input("quant de refri: "))
trefri= qrefri*3
if (item== "L"):
	total= 6 *quant +trefri
	print(round(total,1))

else:
	total= 13.50*quant+trefri
	print(round(total,1))