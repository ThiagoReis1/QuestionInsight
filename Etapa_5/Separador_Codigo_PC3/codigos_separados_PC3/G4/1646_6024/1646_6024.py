from numpy import * 
v = array(eval(input("digite o vetor: ")))
i = 0
c = 0
vetor  = []
for i in range(size(v)):
	if v[i] <= 50:
		vetor.append(i)
		c = c + 1
print(c)
print(array(vetor))