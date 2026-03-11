# faça seu código aqui!
ds = str(input("Informe o dia da semana: "))
qp = int(input("Informe a quantidade de pratos consumidos: "))

if ds =="qua":
	p = 22 - (22 * 0.15)
	vp = p * qp
	print(round(vp, 2))
	
else:
	p = 22
	vp = p * qp
	print(round(vp, 2))