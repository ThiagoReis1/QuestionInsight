unidade = str(input("Digite a unidade: "))
alunos = 0
acum = "ICOMP"
while(unidade.upper() != "S"):
	if(unidade.upper() == "ICOMP"):
		alunos = alunos + 1
	unidade = input("Digite a unidade")
print(alunos)
		