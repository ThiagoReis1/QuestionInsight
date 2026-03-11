alunos = input("Monitoria: ").upper()

contador = 0
qnt = 0

while alunos != "X":
	if alunos == "FT":
		contador += 1
	alunos = input("Monitoria: ").upper()
		
print(contador)
	
	