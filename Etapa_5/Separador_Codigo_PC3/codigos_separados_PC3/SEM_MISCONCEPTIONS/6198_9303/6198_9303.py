altura_luna = 1.65
taxa_luna = 0.02


altura_aluno = float(input("altura: "))
taxa_cresc = float(input("taxa: "))

anos = 0

while (altura_aluno < altura_luna):
	altura_aluno = altura_aluno + taxa_cresc
	altura_luna = altura_luna + taxa_luna
	anos = anos + 1
print(anos)
	
