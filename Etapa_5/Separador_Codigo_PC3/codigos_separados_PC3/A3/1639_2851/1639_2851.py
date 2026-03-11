from numpy import*

vetor_de_alunos = array(eval(input("Digite o vetor: ")))


for elemento in vetor_de_alunos:
	par = 0
	if(elemento % 2 == 0):
		par = par + 1
		
for elemento in vetor_de_alunos:
	v_novo = zeros(par)
	if (elemento % 2 == 0):
		v_novo = elemento[0] + 1
		print(v_novo)