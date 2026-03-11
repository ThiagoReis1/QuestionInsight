altura_cicero = 1.8
taxa_cicero = 0.01
p = float(input("digite a altura:"))
taxa_aluno = float(input("digite a taxa do aluno:"))
anos = 0

while (p <= (altura_cicero+taxa_cicero*anos)):
	if ( taxa_aluno < altura_cicero):
		p = p + taxa_aluno
		anos += 1	
print(anos)