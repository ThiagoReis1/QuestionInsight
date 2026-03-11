from numpy import *
vetor= array(eval(input("elevador parou: ")))
i=0
d=0
an=0
while(i<vetor[i]):
	an=abs(vetor[i]-vetor[i+1])
	an=an+ vetor[i]*3
	i=i+1
print(an)
