from numpy import *
from math import *
p = float(input("Qual o valor? "))
vet = array(eval(input("Insira o vetor: ")))
vet1 = array(eval(input("Insira o outro vetor: ")))
t = p / (p + 1)

vint = 0
vint1 = 0
for i in range (0, size(vet)):
	vint = (abs(vet[i]+vet1[i]) ** t) + vint
norv = vint ** (1/t)
print(round(norv, 3))