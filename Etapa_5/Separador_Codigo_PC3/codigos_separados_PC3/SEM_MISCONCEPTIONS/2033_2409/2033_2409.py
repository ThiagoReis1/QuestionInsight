unidade = input("unidade academica do aluno: ").upper()

soma = 0

while(unidade != "S"):
	if(unidade == "ICOMP"):
		soma = soma + 1
	unidade = input("unidade academica do aluno: ").upper()
print(soma)