altura_cicero = 1.8
taxa_cicero = 0.01

altura_aluno= float(input("Insira a sua altura: "))
taxa_aluno= float(input("Insira sua taxa de crescimento: "))

anos= 0


while (altura_cicero >= altura_aluno):
	altura_cicero= altura_cicero + taxa_cicero
	altura_aluno= altura_aluno + taxa_aluno
	anos= anos + 1 
	
print(anos)