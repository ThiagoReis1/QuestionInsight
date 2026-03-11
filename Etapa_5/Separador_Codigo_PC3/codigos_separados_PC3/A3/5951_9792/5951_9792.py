preco_tapioca = 4.5
preco_salgado = 5.0
preco_acai =12.0 

comida = input("tapioca ou salgado(T/S)?")
qtde = int(input("quantos? "))
qia = int(input("quantos voce pode gastar"))

if comida == "T": 
	total = (qtde * 4.5) + (qia * 12.0)
	
	print(round(total,2))
	
else:
	total = (qtde * 5.0) + (qia * 12.0)
	print(round(total,2))