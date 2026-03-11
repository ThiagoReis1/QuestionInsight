from numpy import*
vetor = array(eval(input("entre com vetor: ")))
i=0
v=0
while (i<size(vetor)):
	if(vetor[i]>80):
		v = v + vetor[i] - 0.15*vetor[i]
	else:
		v = v + vetor[i]
	i = i +1
print(round(v,2))