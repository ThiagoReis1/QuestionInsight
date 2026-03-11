from math import*
k = int(input("Digite o numero de termos: "))
n = 0
y = 0
q = 0
soma = 0
sinal = 1
while(n<k):
	n = n + 1
	soma = (y**3)/(5+q) + sinal*((y+1)**3)/(5+(q+1))
	sinal = sinal*-1
print(round(soma,9))