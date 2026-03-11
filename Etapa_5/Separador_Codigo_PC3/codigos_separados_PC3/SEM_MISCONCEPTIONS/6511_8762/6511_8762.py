# faça seu código aqui!
ent = input("Tipo de entrada: ")
quant = int(input("Informe quantidade desejada: "))
entrada = ent.upper()
if entrada=='B':
	pague = (quant*25.90)
	total = pague - (pague*10/100)
	print(round(total,2))
else: 
	total = quant*25.90
	print(round(total,2))
	