loup = str(input("l ou p:"))
qntdlp = int(input("qntd de piz ou lan"))
qntdr = int(input("qntd derref"))
###################
lanche = 6.00
pizza = 4.50
refr = 3.00
#########################
if loup == "L":
	valor = (qntdlp * lanche) + (qntdr * refr) 
	print(round(valor,2))
if loup == "P":
	valor = (qntdlp * pizza) + (qntdr * refr)
	print(round(valor,2))