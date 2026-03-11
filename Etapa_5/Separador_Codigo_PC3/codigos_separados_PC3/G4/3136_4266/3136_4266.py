from numpy import*
from math import*

v = array(eval(input("Digite o vetor: ")))
i = 0
t = 0

while(i<size(v)):
	t = t + log(v[i]+1)
	i=i+1

m = exp(t/size(v))-1
print(round(m,2))


