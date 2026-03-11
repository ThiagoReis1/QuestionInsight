from numpy import*
magia = array(eval(input("Digite o tipo de magia: ")))
mago = array(eval(input("Digite o nivel do mago: ")))
i = 0
total = 0
while(i < size(magia)):
	if (magia[i].upper() == "GELO"):
		dmago = 2 * mago[i]
	elif (magia[i].upper() == "FOGO"):
		dmago = 3 * mago[i]
	elif (magia[i].upper() == "CHOQUE"):
		dmago = 4 * mago[i]
	elif (magia[i].upper() == "CONJURACAO"):
		dmago = 8 * mago[i]
	elif (magia[i].upper() == "ILUSAO"):
		dmago = 10 * mago[i]
	total = total + dmago
	i = i + 1
print(total)