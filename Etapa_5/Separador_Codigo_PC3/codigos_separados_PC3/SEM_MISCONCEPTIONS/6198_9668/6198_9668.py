altura_luna = 1.65
taxa_luna = 0.02

aluno= float(input("altura do aluno: "))
taxa_aluno= float(input("taxa do aluno: "))

anos= 0

while ( aluno < altura_luna):
	anos = anos + 1
	altura_luna = altura_luna + taxa_luna
	aluno = aluno + taxa_aluno
	
print (anos)