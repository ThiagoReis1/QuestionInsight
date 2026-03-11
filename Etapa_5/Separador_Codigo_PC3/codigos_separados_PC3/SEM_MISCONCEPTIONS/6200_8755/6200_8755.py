altura_cicero = 1.75
taxa_cicero = 0.01
aluno = float(input("digite aqui: "))
taxa = float(input("digite aqui: "))
anos = 0

while (aluno < altura_cicero): 
	altura_cicero = altura_cicero + taxa_cicero
	aluno = aluno + taxa
	anos = anos + 1 
print(anos)