from math import * 
n = int(input("Digite aproximaçao de pi: "))
i = 0 
sinal = 1
piaprox = 0
while(i < n):
    piaprox = piaprox + sinal * 1 / ((4*i + 1) * 3 ** i)
    i = i + 1
    sinal = - sinal
print(round(sqrt(12) * piaprox, 8))