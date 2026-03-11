from numpy import *
n = array(eval(input("notas:")))
vetor = array(eval(input("gastos: ")))
i = 0
caloria = 0
while(i < size(vetor)):
	if(n[i].lower() == "alongamento") or (n[i].lower() == "corrida") or (n[i].lower() == "danca") or (n[i].lower() == "escalada") or (n[i].lower() == "hidroginastica"):
		if(n[i].lower() == "alongamento"):
			caloria = caloria + 3 * vetor[i]
		elif(n[i].lower() == "corrida"):
			caloria = caloria + 10.3 * vetor[i]
		elif(n[i].lower() == "danca"):
			caloria = caloria + 6.7 * vetor[i]
		elif(n[i].lower() == "escalada"):
			caloria = caloria + 9.7 * vetor[i]
		else:
			caloria = caloria + 5.0 * vetor[i]
		i = i + 1
print(round(caloria,2))