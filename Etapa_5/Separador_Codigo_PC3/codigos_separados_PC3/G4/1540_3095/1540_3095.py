from math import*
ang = eval(input())
k = int(input())
sinal = 1
soma = 0
e = 0
f = 0
while (e < k):
	cos = ((ang ** e) / factorial(f)) * sinal
	sinal = sinal * -1
	soma = soma + cos
	e = e + 1
	f = f + 2
print(round(soma, 6))
	