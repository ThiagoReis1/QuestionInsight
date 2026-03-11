from numpy import*
vetor = array(eval(input("vetor: ")))
r = 307
i = 0
n = 0
while(i < size(vetor)):
	if(vetor[i] < r):
		n = n + 1
	i = i + 1
print(r)
print(n)