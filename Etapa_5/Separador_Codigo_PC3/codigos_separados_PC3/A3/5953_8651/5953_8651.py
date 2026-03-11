x = input("qual o seu pedido:")
quant = int(input("quantidade de lanchaes ou pe:"))
quant_refri = int(input("quant de refris:"))

lanche = 6
prat_ex = 13.50
refri = 3

if (x == "L"):
	m = (6 * quant) + (3 * quant_refri)
	print(round(m,1))
	
else:
	n = (13.5 * quant) + (3 * quant_refri)
	print(round(n,1))