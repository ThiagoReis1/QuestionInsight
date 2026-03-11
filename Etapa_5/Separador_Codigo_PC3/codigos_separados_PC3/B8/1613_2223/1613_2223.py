from numpy import *
treina = array(eval(input("Informe um vetor com os treinos feitos: ")))
tempo = array(eval(input("Informe um vetor com o tempo da duração de cada treinamento: ")))

i = 0
total = 0
while(i < size(tempo)):
	if(treina[i] == "ALONGAMENTO"):
		treino = 3.0
	elif(treina[i] == "CORRIDA"):
		treino = 10.3
	elif(treina[i] == "DANCA"):
		treino = 6.7
	elif(treina[i] == "ESCALADA"):
		treino = 9.7
	elif(treina[i] == "HIDROGINASTICA"):
		treino = 5.0
	total = total + treino * tempo[i]
	i = i + 1
print(total)