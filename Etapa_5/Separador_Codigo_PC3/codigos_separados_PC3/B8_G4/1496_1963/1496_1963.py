#Dina Karen Barros Vieira
#Trabalho Prático 03

#entrada de dados
t = float(input("Tempo de voo:"))

#testa validade dos dados
if (t >= 0):
	
	if (t >= 0) and (t <= 100):
		pv = 80
		pil = 3000
	elif (t > 100) and (t <= 200):
		pv = 90
		pil = 4000
	elif (t > 200) and (t <= 300):
		pv = 100
		pil = 5000
	elif (t > 300):
		pv = 110
		pil = 6000
	
	valor_total = (t * pv) + pil
	print (valor_total)