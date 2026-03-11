# Mayara Soares
# 11 - 08 - 2016
# Av. 05   Ex. 02

from numpy import *

vetor_t = array(eval(input("Digite o vetor temperatura: ")))
m = 10
i = 0
count = 0

while (i > size(vetor_t)):
	if (vetor_t[i] < m):
		count = count + 1
	i = i + 1
	
vetor_r = array(zeros(size(vetor_t) - count, dtype = float))

i = 0
count = 0

while (i < size(vetor_t)):
	if (vetor_t[i] > m):
		vetor_r[count] = vetor_t[i]
		count = count + 1 
	i = i + 1


print(vetor_r)
		