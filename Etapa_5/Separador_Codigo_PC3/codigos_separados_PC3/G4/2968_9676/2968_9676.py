q1 = input("L pra lanche e S pra salgado (L/S):\n")

if q1.upper() == "L":
	qntl = int(input("quantidade de lanches:\n"))
	qntr = int(input("quantidade de refris:\n"))
	preco_f = float(qntl*5 + qntr*4)
	print(round(preco_f,2))
if q1.upper() == "S":
	qnts = int(input("quantidade de salgados:\n"))
	qntr = int(input("quantidade de refris:\n"))
	preco_f = float(qnts*3.5 + qntr*4)
	print(round(preco_f,2))