from numpy import*
from math import*
c = array(eval(input(": ")))
i = 0
p = 1
nota = ""
while(i < size(nota) ):
	nota = nota + c[i] * p
	i = i + 1
	p = p + i
m = sum(nota) / p
print(m,2)