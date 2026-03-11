tipo = input("Digite um tipo: ").upper()
quantidade = int(input("Digite uma quantidade: "))
liquido = int(input("Digite uma quantidade: "))
if tipo == "L":
	lanches = quantidade*6.00
	refrigerante = liquido*3.00
	total = lanches + refrigerante
	print(round(total,2))
else:
	pratos = quantidade*13.50
	refrigerante = liquido*3.00
	total = pratos + refrigerante
	print(round(total,2))