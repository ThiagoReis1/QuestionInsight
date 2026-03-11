from numpy import *
n = array(eval(input("notas:")))
vetor = array(eval(input("gastos: ")))
i = 0
caloria = 0
while(i < size(vetor)):
	if(n[i].lower() == "alongamento") or (n[i].lower() == "corrida") or (n[i].lower() == "danca") or (n[i].lower() == "escalada") or (n[i].lower() == "hidroginastica"):
		if(n[i].lower() == "alongamento"):
			caloria = caloria + 1.25 * vetor[i]
		elif(n[i].lower() == "corrida"):
			caloria = caloria + 2.60 * vetor[i]
		elif(n[i].lower() == "danca"):
			caloria = caloria + 1.80 * vetor[i]
		elif(n[i].lower() == "escalada"):
			caloria = caloria + 0.85 * vetor[i]
		else:
			caloria = caloria + 3.20 * vetor[i]
		i = i + 1
print(round(caloria,2))