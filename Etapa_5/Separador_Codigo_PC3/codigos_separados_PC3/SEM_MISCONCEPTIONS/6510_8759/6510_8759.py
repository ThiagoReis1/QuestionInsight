# faça seu código aqui!
dia= input("Que Dia Da Semana eh Hoje: ")
quant= int(input("quantos pratos: "))
desconto= (quant* 22) *(15/100)
if dia == "qua":
	total= quant*22 - desconto
	
	print(round(total,2))
else:
	total= quant* 22
	
	print(round(total, 2))