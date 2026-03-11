from numpy import*
vetor= array(eval(input('vetor: ')))
sb=0
x=0
for i in range (size(vetor)):
	if vetor[i] <= 50:
		sb= sb+1
nulo= zeros(sb, dtype=int)
for i in range (size(vetor)):
	if vetor [i]<=50:
		nulo[x] = i
		x = x+1
print(sb)
print(nulo)

		
	
	