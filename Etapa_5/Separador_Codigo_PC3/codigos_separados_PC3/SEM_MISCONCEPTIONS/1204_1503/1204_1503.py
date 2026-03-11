from numpy import*
vetor = array(eval(input("Valor do salto:")))
recorde = 2.5
i = 0
t = 0
while i< size(vetor):
	if(vetor[i]<recorde):
		t = t + 1
	i = i + 1
print(recorde)
print(t)