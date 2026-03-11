from numpy import*

v = array(eval(input("Digitar vetor: ")))

r = 74.08
print(r)
i = 0
quantidade = 0
while(i < size(v)):
	if(v[i] > r):
		quantidade = quantidade + 1
	i = i + 1
print(quantidade)