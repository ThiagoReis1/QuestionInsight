from numpy import*
vetor=array(eval(input("")))
pontos=0
i=0
while i<size(vetor):
	if vetor[i]==1:
		pontos= pontos+10
	if vetor[i]==2:
		pontos=pontos+5
	if vetor[i]==3:
		pontos= pontos+0
	if vetor[i]==4:
		pontos=pontos+5
	if vetor[i]==5:
		pontos=pontos+20
	if vetor[i]==6:
		pontos=pontos+10
	i= i+1
print(round(pontos,2))
	