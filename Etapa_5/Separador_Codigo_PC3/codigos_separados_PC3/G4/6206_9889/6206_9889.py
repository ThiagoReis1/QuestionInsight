ni = int(input("Digite os numeros dentro de um intervalo: "))

qni = 0 #quantidade de numeros nesse intervalo 

while (ni != -1):
	if (ni>=0 and ni <=25):
		qni = qni + 1

	ni = int(input("Digite os numeros dentro de um intervalo: "))
	
print(qni)