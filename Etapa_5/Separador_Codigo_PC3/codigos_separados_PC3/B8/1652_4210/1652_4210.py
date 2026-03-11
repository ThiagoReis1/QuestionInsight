from numpy import*
etnia = input("insira a etnia: ").upper().split(',')
alunos = zeros(5,dtype=int)

for i in etnia:
	if(i=="B"):
		alunos[0] = alunos[0] + 1
	elif(i=="PA"):
		alunos[1] = alunos[1] + 1
	elif(i=="PR"):
		alunos[2] = alunos[2] + 1
	elif(i=="A"):
		alunos[3] = alunos[3] + 1
	elif(i=="I"):
		alunos[4] = alunos[4] + 1
print(max(alunos))
print(alunos)