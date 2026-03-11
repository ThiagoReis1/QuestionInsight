lanche = input("digite o lanche: ")
pizza = int(input("digite a qtd: "))
refri = int(input("digite a qtd: "))

valorL= 6.00
valorP = 4.50
valorR = 3.00

if lanche == "P":
	valortotal = (pizza * valorP) + (refri * valorR)
	print(round(valortotal,2))
else:
	valortotal = (pizza * valorL) + (refri * valorR)
	print(round(valortotal, 2))
	