from numpy import *
 
vet = array(eval(input()))
 
A = min(vet)
B = max(vet)
C = 0.65 * A + 0.35 * B
D = 0.45 * A + 0.55 * B
 
saida = zeros(2, dtype=int)
 
i = 0
x1 = 0
x2 = 0
while (i < size(vet)):
    if ((vet[i] >= A) and (vet[i] < C)):
        x1 = x1 + 1
    if ((vet[i] >= C) and (vet[i] < D)):
        x2 = x2 + 1
    i = i + 1
 
 
saida[0] = x1
saida[1] = x2
 
print (saida)