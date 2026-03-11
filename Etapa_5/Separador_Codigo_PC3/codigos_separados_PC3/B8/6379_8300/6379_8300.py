from numpy import*
notas = input("Digite as notas dos alunos:")
contador = [0,0,0,0,0]

notas_separadas = notas.split(",")
for nota in notas_separadas:
	if nota == "A":
		contador[0] +=1
	elif nota == "B":
		contador[1] +=1
	elif nota == "C":
		contador[2] +=1
	elif nota == "D":
		contador[3] +=1
	elif nota == "E":
		contador[4] +=1
print(array(contador))
