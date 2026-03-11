lanche=input(" 'L' para lanche e 'S' para salgado: ").upper()
quant= int(input("quantidade de lanche: "))
refri= int(input("quantidade de refri: "))


if lanche=="L":
	valor= (quant*5.00)+(refri*4.00)
	print(valor)
else:
	valor2= (quant*3.50)+(refri*4.00)
	print(valor2)

