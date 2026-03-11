from numpy import*
vetor=array(eval(input("digite a qntd de alunos:  ")))
soma=0
for i in vetor:
	if i!=99:
		soma=soma+i
	elif i==99:
		soma=(soma*2)
print(soma)