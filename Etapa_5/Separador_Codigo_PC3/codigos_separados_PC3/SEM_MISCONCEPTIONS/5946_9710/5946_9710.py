nome = str(input("L para lanche ou P para pizza:"))
lanche = int(input("quant lancche:"))
refri = int(input("quant refri:"))
pizza = int(input("quant pizza"))
if (nome.upper()== "P") :
	total = (lanche*6.00)+(pizza*6.00)
	prin(round(total,2))
if (nome.upper() == "L"):
	
	total = (refri*3.00)+(lanche*6.00)
	print(round(total,2))


