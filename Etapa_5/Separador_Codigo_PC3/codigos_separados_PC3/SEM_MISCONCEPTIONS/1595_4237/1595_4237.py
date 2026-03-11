from numpy import *

notas = array(eval(input("Notas:")))
j = 0 
p = 0

for i in range(size(notas)):
	if(notas[i] != min(notas)):
		p = p + 1

c = zeros(p)
for i in range(size(notas)):
	if(notas[i] != min(notas)):
		c[j] = notas[i]
		j = j + 1 
		
mediafinal = sum(c)/size(c)
print(round(mediafinal,2))