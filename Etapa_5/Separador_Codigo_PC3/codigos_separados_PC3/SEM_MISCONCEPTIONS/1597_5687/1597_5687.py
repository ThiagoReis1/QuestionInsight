
from numpy import*

v = array(eval(input("informe o vetor:")))

descontos = 0 
i = 0

while(i < size(v)):
	if(v[i] >80):
		descontos = descontos + 5
	i = i + 1
print(round(sum(v) - descontos, 2))
