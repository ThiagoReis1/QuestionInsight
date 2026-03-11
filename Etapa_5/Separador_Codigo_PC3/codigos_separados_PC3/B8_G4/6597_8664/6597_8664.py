N = int(input("Quantidade de funcionarios: "))

QVA = 0
QVB = 0
QVC = 0

cont = 1

while (cont <= N):
	tec = input("Qual sera a tecnica: ").upper()
	if (tec == "A".upper()):
		QVA += 1
	elif (tec == "B".upper()):
		QVB +=1
	elif (tec == "C".upper()):
		QVC += 1
		
	cont += 1
	
print("A= ", QVA)
print("B= ", QVB)
print("C= ", QVC)
		
		