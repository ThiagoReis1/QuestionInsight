from numpy import *

ac = array(eval(input("Informe o vetor: ")))

k = 0
i = 0

while i < size(ac):
	if(ac[0]>ac[i]):
		k = k + 1
		print(i)
		
	i = i + 1
print(k)
	
	
