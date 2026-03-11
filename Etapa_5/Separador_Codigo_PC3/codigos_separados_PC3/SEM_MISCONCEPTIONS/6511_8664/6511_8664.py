# faça seu código aqui!

entrada = input("Tipo de entrada: ")
quantidade_de_entradas = int(input("Quantidade de entradas: "))

if entrada.upper() != "B":
	menu = 25.90
	valor_total1 = menu*quantidade_de_entradas 
	print(round(valor_total1, 2))
else:
	menu = 25.90
	valor_total1 = menu*quantidade_de_entradas
	valor_total2 = (menu*quantidade_de_entradas)-(valor_total1*(10/100))
	print(round(valor_total2, 2))
   

