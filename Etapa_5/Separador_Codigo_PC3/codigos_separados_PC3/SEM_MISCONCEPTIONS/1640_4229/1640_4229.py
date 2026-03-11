from numpy import*
vetor = array(eval(input("quantidade de alunos matriculados em cada turma: ")))
impar = 0
outrovetor=zeros(size(vetor),dtype=int)
for i in range(size(vetor)):
	if(vetor[i]%2!=0):
		impar = impar + 1
		outrovetor[i] = i
a = '0'
grupoimpar=.split(outrovetor,a)
print(impar)
print(grupoimpar)