digil_p= input("Digite L se for lanche ou P se for prato executivo: ")
qnt_loup= int(input("Digite a quantidade de lanches: "))
qnt_refri= int(input("Digite a quantidade de refrigerantes: "))

lanche= 6.00
pratoe= 13.50
refri= 3.00

valor_total= (qnt_loup* 6.00)+ (qnt_refri* 3.00)
valor_totall= (qnt_loup * 13.50)+(qnt_refri* 3.00)


if digil_p == "L":
	valor_total= (qnt_loup* 6.00)+ (qnt_refri* 3.00)
	print(round(valor_total,2))
else:
	valor_totall= (qnt_loup*13.50)+ (qnt_refri*3.00)
	print(round(valor_totall,2))