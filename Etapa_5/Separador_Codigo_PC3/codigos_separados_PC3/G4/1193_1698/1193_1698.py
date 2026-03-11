from numpy import*
from math import *

vetor = array(eval(input("Digite aqui o vetor:")))

i = 0
k = 0
while(i < size(vetor)):
	if(vetor[i] < -100):
		k = k + 1
	i = i + 1
p = size(vetor)
num = p - k
vetor1 = zeros(num, dtype=float)
a=0
b=0
while(a < num):
	if(vetor[b] > -100):
		vetor1[a] = vetor1[a] + vetor[b]
		a = a + 1
	b = b + 1
print(vetor1)