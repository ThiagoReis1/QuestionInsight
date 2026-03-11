from numpy import*

aluno = array(eval(input()))

cont = 0
for i in range(0,size(aluno)):
	if aluno[i]<70:
		cont +=1
		
v = zeros(cont, dtype=int)
j = 0
for i in range(0, size(aluno)):
	if aluno[i] < 70:
		v[j] = i
		j +=1
print(cont)
print(v)