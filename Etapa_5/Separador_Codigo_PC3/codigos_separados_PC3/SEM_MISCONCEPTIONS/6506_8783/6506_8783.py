qte=int(input("quantidade de pratos consumidos:"))
sobremesa=input("deseja sobremesa?(S/N)")
if (sobremesa.upper()=="S"):
	valor=qte*40
	desc=valor*(5/100)
	total=valor-desc
	print(round(total,2))
if (sobremesa.upper()=="N"):
	total=qte*40
	print(round(total,2))