altura_bia = 1.69
taxa_bia = 0.01

altura_aluno= float(input(''))
taxa_aluno = float(input(''))
cont = 0

while altura_aluno < altura_bia :
	altura_bia += taxa_bia
	altura_aluno += taxa_aluno
	cont += 1
print(cont)