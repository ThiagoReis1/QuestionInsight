from numpy import*
from math import*

p = array(eval(input("Digite o primeiro vetor: ")))
q = array(eval(input("Digite o segundo vetor: ")))

i = 0
s = 0

while (i < size(p)):
	s = s + ((p[i] - q[i]) ** 2 )
	i = i + 1
	
d = sqrt(s)
sim = 1 / (1 + d)

print(round(d , 4))
print(round(sim , 2))