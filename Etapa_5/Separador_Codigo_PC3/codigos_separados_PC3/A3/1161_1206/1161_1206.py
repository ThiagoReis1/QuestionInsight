hordaZ= float(input("Números de Zumbi: "))
numH= float(input("Número de habitantes: "))
captrans= float(input("Capacidade de transformação: "))
extZ= float(input("Extermínio de Zumbis por dia: "))

t=0


while(numH <= hordaZ):
	hordaZ= (hordaZ + captrans)- extZ 
	numH2 = numH - captrans
	t=t+1
	print(t)