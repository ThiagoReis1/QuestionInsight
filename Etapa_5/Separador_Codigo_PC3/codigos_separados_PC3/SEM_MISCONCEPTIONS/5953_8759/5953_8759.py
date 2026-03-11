qual= input("Lanche ou prato executivo: ")
quant= int(input("quantos: "))
refri= int(input("quantos refrigerantes"))

if qual.upper()=="L":
	total= (quant * 6.00) + (refri *3)
	
	print(total)
else:
	total= (quant * 13.50) + (refri *3)
	print(total)