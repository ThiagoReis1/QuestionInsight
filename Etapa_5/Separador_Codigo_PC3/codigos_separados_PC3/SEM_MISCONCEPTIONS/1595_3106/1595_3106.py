from numpy import*
notas = array(eval(input("Notas: ")))

i = 0
media = 0
alunos = 0

while(i<size(notas)):
	if(notas[i] != min(notas)):
		media = media + notas[i]
		alunos = alunos + 1
	i = i + 1
	
if(alunos == 0):
	media = notas[0]
	alunos = 1
	
print(media/alunos)