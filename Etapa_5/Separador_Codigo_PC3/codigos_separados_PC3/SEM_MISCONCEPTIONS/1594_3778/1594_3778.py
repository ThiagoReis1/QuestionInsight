from numpy import*
vetor = array(eval(input()))
i = 0
dano = 0
while i < len(vetor):
	dano = dano + (vetor[i]*(i+1))
	i = i + 1
print(dano)