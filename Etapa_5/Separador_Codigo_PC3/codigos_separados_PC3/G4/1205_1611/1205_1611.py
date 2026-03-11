from numpy import *
v = array(eval(input("Digite o vetor:")))
i = 0
q = 0
while(i < size(v)):
	if(v[i] > 8.95):
		q = q + 1
	i = i + 1
print("8.95")
print(q)