from numpy import *
frequencia = array(eval(input("Insira frequencia de aulas: ")))

aprovado = 0
for i in frequencia:
	if(i >= 70):
		aprovado += 1
print(aprovado)

v = zeros(aprovado, dtype=int)
x = 0
i = 0
while(x < size(frequencia)):
	if(frequencia[x] >= 70):
		v[i] = x
		i += 1
	x += 1
print(v)