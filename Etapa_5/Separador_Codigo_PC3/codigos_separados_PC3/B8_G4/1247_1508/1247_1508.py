from numpy import*

vetor = array(eval(input(" ")))
a = min(vetor)
b = max(vetor)
c = (0.75*a)+(0.25*b)
d = (0.25*a)+(0.75*b)

u = 0
w = 0

x = array(zeros(2, dtype=int))


for i in range(size(vetor)):
	if(vetor[i]>=a) and (vetor[i]<c):
		u = u + 1
		x[0]= u
	elif(vetor[i]>=d) and (vetor[i]<b):
		w = w + 1
	x[1] = w
print(x)