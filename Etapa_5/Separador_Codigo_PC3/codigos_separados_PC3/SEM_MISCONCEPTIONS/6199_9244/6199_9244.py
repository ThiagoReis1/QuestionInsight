altura_aluno = float(input("digite o numero: "))
taxa_aluno = float(input("digite o numero: "))
 
altura_cicero = 1.8
taxa_cicero = 0.01
anos = 0

while (altura_aluno < altura_cicero):
	altura_aluno = altura_aluno + taxa_aluno
	altura_cicero = altura_cicero + taxa_cicero
	anos = anos + 1
print(anos)