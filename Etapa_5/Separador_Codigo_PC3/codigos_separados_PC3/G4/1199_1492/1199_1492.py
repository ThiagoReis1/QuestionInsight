from numpy import*
vetor = array(eval(input("")))
i = 0
t = 0
while(i < size(vetor)):
	if (vetor[i] <= 10):
		t = t + 1
	i = i + 1
v = array(zeros(t , dtype = float))
i = 0
k = 0
while(i < size(vetor)):
	if( vetor[i] > 10 ):
		vetor [k] = v [i]
		k = k + 1
	i = i + 1
print ( v )			