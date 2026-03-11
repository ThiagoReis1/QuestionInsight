x = float(input())
k = int(input())
i=1
t=3
sinal = -1
soma = x
while(i<k):
	soma = soma + (sinal) * (x**t)/t
	i = i + 1
	t=t +2
	sinal = - sinal
print(round(soma,6))