from numpy import*
t=array(eval(input("vetor com a quantidade de alunos")))
ncinco=0 # zera contador de  cincos
j=0 #contador para o vetor de turmas de cincos
for i in range(size(t)):
	if(t[i] % 5==0):
		ncinco=ncinco+1
	
v=zeros(ncinco,dtype=int)
for i in range(size(t)):
	if(t[i] % 5==0):
		v[j]=i
		j=j+1
print(ncinco)
print(v)
		