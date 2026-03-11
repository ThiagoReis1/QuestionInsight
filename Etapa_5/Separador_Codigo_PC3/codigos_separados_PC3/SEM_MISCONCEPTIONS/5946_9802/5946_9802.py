l_p = input("lanche ou pizza (L/P): ")
quant1 = int(input("quantidade de comida: "))
quant2 = int(input("quantidade de refri: "))

if l_p == "L":
	lanche = quant1 * 6.00
	refri = quant2 * 3.00
	precf = lanche + refri
	print(round(precf,2))
else:
	pizza = quant1 * 4.50
	refri = quant2 * 3.00
	precf = pizza + refri
	print(round(precf,2))